from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["email", "name", "phone"]
    # readonly_fields = ["email", "name", "phone"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (("Personal info"), {"fields": ("name", "phone")}),
        (
            ("Permissions"), {
                "fields": ("is_active", "is_staff", "is_superuser")}
        ),

    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "name", "phone",  "password1", "password2")}),
    )


admin.site.register(User, UserAdmin)
