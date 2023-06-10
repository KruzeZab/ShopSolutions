from django.contrib.auth import get_user_model
from django.db import models

from helpers.models import BaseModel, Image


User = get_user_model()


class Category(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Tag(BaseModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Product(BaseModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="products"
    )
    tags = models.ManyToManyField(Tag, blank=True)

    _meta_title = models.CharField(
        verbose_name="meta title", max_length=100, null=True, blank=True
    )
    _meta_description = models.CharField(
        verbose_name="meta description", max_length=255, null=True, blank=True
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    excerpt = models.CharField(max_length=255)
    actual_price = models.PositiveIntegerField(help_text="Amount in cents")
    offer_price = models.PositiveIntegerField(
        null=True, blank=True, help_text="Amount in cents"
    )

    total_quantity = models.PositiveIntegerField()
    sold_quantity = models.PositiveIntegerField(default=0)

    images = models.ManyToManyField(Image, blank=True)

    general_details = models.JSONField(default=dict, blank=True)
    product_details = models.JSONField(default=dict, blank=True)

    description = models.TextField(blank=True, null=True)
    added_by = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="products"
    )
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.DRAFT  # type: ignore
    )

    def __str__(self):
        return self.title

    @property
    def price(self):
        """
        Returns offer price if available else actual price
        """
        if self.offer_price:
            return self.offer_price

        return self.actual_price

    @property
    def available_quantity(self):
        """
        Returns remaining quantity
        """
        return self.total_quantity - self.sold_quantity

    @property
    def meta_title(self):
        return self._meta_title or self.title

    @property
    def meta_description(self):
        return self._meta_description or self.excerpt

    def is_published(self):
        return self.status == self.Status.PUBLISHED

    def is_draft(self):
        return self.status == self.Status.DRAFT


class Cart(BaseModel):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        ORDERED = "ordered", "Ordered"

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="carts")
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)

    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PENDING  # type: ignore
    )

    def __str__(self):
        return f"{self.user} - {self.product.title}"

    @property
    def total_price(self):
        return self.product.price * self.quantity

    def is_ordered(self):
        return self.status == self.Status.ORDERED

    def is_pending(self):
        return self.status == self.Status.PENDING


class Order(BaseModel):
    class Staus(models.TextChoices):
        PENDING = "pending", "Pending"
        DELIVERED = "delivered", "Delivered"

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="orders")
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="orders"
    )
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()
    status = models.CharField(
        max_length=20, choices=Staus.choices, default=Staus.PENDING  # type: ignore
    )

    def __str__(self):
        return f"{self.user} - {self.product.title}"

    @property
    def total_price(self):
        return self.price * self.quantity

    @property
    def shipping_address(self):
        return self.user.address  # type: ignore

    def is_delivered(self):
        return self.status == self.Staus.DELIVERED

    def is_pending(self):
        return self.status == self.Staus.PENDING
