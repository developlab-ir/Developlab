from django import forms
from .models import Question,Answer
from dal import autocomplete


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("title","type","description","categories")

        widgets = {
                    "title": forms.TextInput(
                        attrs={
                            "class": "form-control",
                            "placeholder": "عنوان پرسش",
                        }
                    ),

                    "type": forms.Select(
                        attrs={
                            "class": "form-control",
                            "placeholder": "نوع پرسش",
                        }
                    ),
        
                    "description": forms.Textarea(
                        attrs={
                            "class": "form-control",
                            "rows": 3,
                            "placeholder": "توضیحات در مورد پرسش",
                        }
                    ),
                    "categories": autocomplete.ModelSelect2Multiple(
                        url="core:category-autocomplete",
                                        attrs={
                                            "class": "form-select",
                                            "data-placeholder": "دسته‌بندی را انتخاب کنید...",
                                        },
                    )
        }