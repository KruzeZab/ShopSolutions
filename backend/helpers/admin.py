from django.contrib import admin
from django.db import models
from django.utils.html import format_html

from django_json_widget.widgets import JSONEditorWidget

from .models import Image


class BaseModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {"widget": JSONEditorWidget},
    }


@admin.register(Image)
class ImageAdmin(BaseModelAdmin):
    list_display = ("_image", "_name")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "_image",
                    "image",
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
    readonly_fields = ("_image", "created_at", "updated_at")

    def _image(self, obj):
        return format_html('<img src="{}" width="100px" />'.format(obj.image.url))

    def _name(self, obj):
        return obj.image.name
