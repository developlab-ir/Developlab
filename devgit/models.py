from django.db import models


class Repository(models.Model):
    owner = models.ForeignKey(
        "accounts.CustomUser",
        on_delete=models.CASCADE,
        related_name="repositories"
    )

    gitea_repo_id = models.PositiveIntegerField(
        unique=True
    )

    name = models.CharField(
        max_length=255,
        verbose_name="نام مخزن"
    )

    description = models.TextField(
        blank=True
    )

    is_private = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "مخزن"
        verbose_name_plural = "مخازن"
        db_table = "repositories"

    def __str__(self):
        return self.name