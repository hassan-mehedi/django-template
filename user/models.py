from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    MALE = "Male"
    FEMALE = "Female"
    OTHERS = "Others"
    NOT_SPECIFIED = "N/A"

    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHERS, "Others"),
        (NOT_SPECIFIED, "Not Specified"),
    ]

    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(_("first name"), max_length=50, blank=True)
    last_name = models.CharField(_("last name"), max_length=50, blank=True)
    email = models.EmailField(_("email address"), max_length=50, unique=True)
    age = models.PositiveIntegerField(blank=True, default=0)
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, default=NOT_SPECIFIED, blank=True
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "users"
        verbose_name = _("user")
        verbose_name_plural = _("users")
        constraints = [
            models.UniqueConstraint(fields=["email"], name="unique_email"),
            models.UniqueConstraint(fields=["user_id"], name="unique_user_id"),
        ]

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.first_name
