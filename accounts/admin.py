from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm,CustomUserCreationForm


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = (
        "__str__",
        "display_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "date_joined",
        "last_login",
        "website",
        )
    list_editable = ("display_name","is_active","is_staff",)
    
    list_filter = ("is_active","is_staff","is_superuser","date_joined","last_login")
    
    list_per_page = 20

    date_hierarchy = "date_joined"
    
    search_fields = ("display_name","first_name","last_name","username")

    empty_value_display = "----"

    add_form = CustomUserCreationForm
    
    form = CustomUserChangeForm

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "email", "phone_number", "first_name", "last_name", "password1", "password2"),
            },
        ),
    )
    
    fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username","email","phone_number")
            },
        ),
        (
            None,
            {
                "classes": ("wide",),
                "fields": (("first_name","last_name",),"display_name",)
            },
        ),
        (
            "گزینه های پیشرفته",
            {
                "classes": ("collapse",),
                "fields": ("avatar","website","groups","user_permissions","gitea_user_id","bio",)
            },
        ),
        (
            "تاریخ ها",
            {
                "classes": ("wide",),
                "fields": ("date_joined","last_login",)
            },
        ),
    )
    
    readonly_fields = ("date_joined","last_login","gitea_user_id")