from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("email",)  # Add other fields you want to show in creation form


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ("email",)  # Add other fields you want to show in change form


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ("email", "age", "gender", "is_staff", "is_active", "is_superuser")
    list_filter = ("is_staff", "is_active", "is_superuser", "gender")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("age", "gender")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "first_name",
                    "last_name",
                    "password1",
                    "password2",
                    "age",
                    "gender",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                ),
            },
        ),
    )

    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


# Unregister the default UserAdmin if it was previously registered
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

# Register your custom UserAdmin
admin.site.register(User, CustomUserAdmin)
