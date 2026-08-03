from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


def avatar_upload_path(instance, filename):
    """Dynamic Avatar Upload Path"""

    username = instance.username or "new_user"
    current_time = timezone.now().strftime("%Y/%m/%d/%H%M%S")

    return f"users/avatars/{username}/{current_time}/{filename}"


class CustomUser(AbstractUser):

    email = models.EmailField(
        verbose_name="ایمیل",   
        unique=True,
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        verbose_name="شماره تلفن",
        max_length=13,
        unique=True,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^\+989\d{9}$",
                message="شماره تلفن باید با فرمت +989xxxxxxxxx باشد.",
            )
        ],
    )

    avatar = models.ImageField(
        verbose_name="آواتار",
        upload_to=avatar_upload_path,
        blank=True,
        null=True,
    )

    display_name = models.CharField(
        verbose_name="نام نمایشی",
        max_length=100,
        blank=True,
        null=True,
    )

    bio = models.TextField(
        verbose_name="بیوگرافی",
        blank=True,
        null=True,
    )

    location = models.CharField(
        verbose_name="مکان",
        max_length=100,
        blank=True,
        null=True,
    )

    website = models.URLField(
        verbose_name="وب‌سایت",
        null=True,
        blank=True,
    )

    gitea_user_id = models.PositiveIntegerField(
        verbose_name="شناسه کاربر در Gitea",
        unique=True,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "حساب کاربری"
        verbose_name_plural = "حساب‌های کاربری"
        db_table = "accounts"
        ordering = ["-date_joined"]

    def __str__(self):
        return (
            self.display_name
            or self.get_full_name()
            or self.username
        )

    def clean(self):
        super().clean()

        self.email = self.email or None
        self.phone_number = self.phone_number or None

        if not self.email and not self.phone_number:
            raise ValidationError(
                "حداقل یکی از ایمیل یا شماره تلفن باید وارد شود."
            )