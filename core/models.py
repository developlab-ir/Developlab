from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    name = models.CharField(verbose_name="نام (انگلیسی)",max_length=110)

    verbose_name = models.CharField(
        verbose_name="نام (فارسی)",
        max_length=110,
        blank=True,
        null=True
    )

    slug = models.SlugField(
        verbose_name="شناسه",
        unique=True,
        blank=True
    )

    seo_description = models.TextField(verbose_name="توضیحات(مربوط به سئو)",help_text="این توضیحات برای سئو و جستجوی بهتر در خود سایت است",blank=True,null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        if self.pk is None and self.slug:
            original_slug = self.slug
            counter = 1
            while Category.objects.filter(slug=self.slug).exists():
                self.slug = f"{original_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    class Meta:
        db_table = "categories"
        verbose_name = "برچسب"
        verbose_name_plural = "برچسب ها"

    def __str__(self):
        return self.verbose_name or self.name