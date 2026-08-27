from django import forms
from .models import Question,Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ("title","type","description")

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
        }