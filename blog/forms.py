from .models import Post
from django import forms
from dal import autocomplete


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            "title",
            "summary",
            "description",
            "thumbnail",
            "categories",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "عنوان پست",
                }
            ),

            "summary": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "توضیح کوتاه درباره پست",
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 15,
                    "placeholder": "محتوای پست...",
                }
            ),

            "thumbnail": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),

            "categories": autocomplete.ModelSelect2Multiple(
                url="core:category-autocomplete",
                attrs={
                    "class": "form-select",
                    "data-placeholder": "دسته‌بندی را انتخاب کنید...",
                },
            ),
        }