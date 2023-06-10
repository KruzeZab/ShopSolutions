from django.contrib import admin
from django.http.request import HttpRequest

from helpers.admin import BaseModelAdmin

from .models import Category, Tag, Product, Cart, Order


class CatTagAdmin(BaseModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "title",
                    "slug",
                )
            },
        ),
        (
            "Audit",
            {
                "fields": (
                    "is_active",
                    "created_at",
                    "updated_at",
                    "meta",
                ),
            },
        ),
    )
    readonly_fields = ("created_at", "updated_at")


@admin.register(Category)
class CategoryAdmin(CatTagAdmin):
    pass


@admin.register(Tag)
class TagAdmin(CatTagAdmin):
    pass


@admin.register(Product)
class ProductAdmin(BaseModelAdmin):
    list_display = (
        "title",
        "category",
        "actual_price",
        "offer_price",
        "total_quantity",
        "sold_quantity",
    )
    list_filter = ("category",)
    search_fields = ("title",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "category",
                    "tags",
                    "title",
                    "slug",
                    "excerpt",
                    "actual_price",
                    "offer_price",
                    "total_quantity",
                    "sold_quantity",
                    "images",
                    "general_details",
                    "product_details",
                    "description",
                )
            },
        ),
        (
            "Meta",
            {
                "fields": (
                    "_meta_title",
                    "_meta_description",
                )
            },
        ),
        (
            "Audit",
            {
                "fields": (
                    "is_active",
                    "created_at",
                    "updated_at",
                    "added_by",
                    "meta",
                ),
            },
        ),
    )
    readonly_fields = ("created_at", "updated_at", "added_by", "sold_quantity")


@admin.register(Cart)
class CartAdmin(BaseModelAdmin):
    list_display = ("user", "product", "quantity", "total_price")
    list_filter = ("user", "product")
    search_fields = ("user__username", "product__title")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "product",
                    "quantity",
                    "total_price",
                    "status",
                )
            },
        ),
        (
            "Audit",
            {
                "fields": (
                    "is_active",
                    "created_at",
                    "updated_at",
                    "meta",
                ),
            },
        ),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(Order)
class OrderAdmin(BaseModelAdmin):
    list_display = ("user", "product", "quantity", "total_price")
    search_fields = ("user__email", "product__title")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "product",
                    "quantity",
                    "total_price",
                    "shipping_address",
                    "status",
                )
            },
        ),
        (
            "Audit",
            {
                "fields": (
                    "is_active",
                    "created_at",
                    "updated_at",
                    "meta",
                ),
            },
        ),
    )

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
