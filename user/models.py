from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    # Choices
    genders = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Others"),
        ("N/A", "Not Specified"),
    )

    # Fields
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    age = models.PositiveIntegerField(blank=True, default=0)
    gender = models.CharField(max_length=10, choices=genders, blank=True, default="N/A")
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        db_table = "users"
        constraints = [
            models.UniqueConstraint(fields=["email"], name="unique_email"),
            models.UniqueConstraint(fields=["user_id"], name="unique_user_id"),
            models.CheckConstraint(
                check=models.Q(gender__in=["Male", "Female", "Others", "N/A"]),
                name="gender_check",
            ),
        ]

    def __str__(self):
        return self.username
