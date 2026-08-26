from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = "__all__"

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username","email","phone_number","first_name","last_name","password1","password2")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        placeholders = {
            'username': 'نام کاربری',
            'email': 'ایمیل',
            'phone_number': 'شماره تلفن',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'password1': 'رمز عبور',
            'password2': 'تکرار رمز عبور',
        }
        
        for field_name, field in self.fields.items():
            field.help_text = None
            
            field.label = None
            
            placeholder_text = placeholders.get(field_name, field_name.replace('_', ' ').title())
            field.widget.attrs.update({
                'placeholder': placeholder_text,
                'class': 'form-control'
            })
            
from django import forms
from .models import CustomUser

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "bio", "avatar", "display_name", "location", "website")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        placeholders = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'bio': 'بیوگرافی',
            'avatar': 'انتخاب تصویر پروفایل',
            'display_name': 'نام نمایشی',
            'location': 'مکان',
            'website': 'وبسایت شخصی',
        }
        
        for field_name, field in self.fields.items():
            field.help_text = None
            field.label = ''
            
            placeholder_text = placeholders.get(field_name, field_name.replace('_', ' ').title())
            
            if field_name == 'bio':
                field.widget.attrs.update({
                    'placeholder': placeholder_text,
                    'class': 'form-control',
                    'rows': 4,
                    'cols': 50
                })
            elif field_name == 'avatar':
                field.widget.attrs.update({
                    'class':'form-control',
                    'accept': 'image/*'
                })
                continue
            elif field_name == 'website':
                field.widget.attrs.update({
                    'placeholder': placeholder_text,
                    'class': 'form-control',
                    'type': 'url'
                })
            else:
                field.widget.attrs.update({
                    'placeholder': placeholder_text,
                    'class': 'form-control'
                })

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        placeholders = {
            'username': 'نام کاربری یا ایمیل',
            'password': 'رمز عبور',
        }
        
        for field_name, field in self.fields.items():
            field.help_text = None
            field.label = '' 
            
            placeholder_text = placeholders.get(field_name, field_name.replace('_', ' ').title())
            field.widget.attrs.update({
                'placeholder': placeholder_text,
                'class': 'form-control'
            })