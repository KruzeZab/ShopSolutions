from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm

from helpers.admin import BaseModelAdmin

from .models import User, Address


@admin.register(User)
class UserAdmin(BaseModelAdmin):
    list_display = ("email", "first_name", "last_name", "phone_number", "is_staff")
    search_fields = ("email",)
    form = UserChangeForm
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "phone_number",
                    "first_name",
                    "last_name",
                    "password",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                ),
            },
        ),
        (
            "Audit",
            {
                "fields": (
                    "last_login",
                    "created_at",
                    "updated_at",
                    "meta",
                ),
            },
        ),
    )
    readonly_fields = ("last_login", "created_at", "updated_at")


@admin.register(Address)
class AddressAdmin(BaseModelAdmin):
    list_display = ("user", "state", "city", "street", "postal_code")
    search_fields = ("user__email",)
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "user",
                    "state",
                    "city",
                    "street",
                    "postal_code",
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
