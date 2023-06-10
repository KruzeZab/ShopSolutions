from django.db import models


class BaseQuerySet(models.QuerySet):
    def _all(self):
        return self.filter(is_active=True)


class BaseManager(models.Manager):
    def get_queryset(self):
        return BaseQuerySet(self.model, using=self._db)

    def _all(self):
        return self.get_queryset()._all()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    meta = models.JSONField(default=dict, blank=True)

    objects = BaseManager()

    class Meta:
        abstract = True

    def delete(self, force_delete=False, *args, **kwargs):
        if force_delete:
            return super().delete(*args, **kwargs)
        self.is_active = False
        self.save()


class Image(BaseModel):
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.image.name
