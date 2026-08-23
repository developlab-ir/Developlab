from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name","verbose_name","slug","seo_description")