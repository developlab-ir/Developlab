from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from .models import CustomUser
from django import forms


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = "__all__"

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username","email","phone_number","first_name","last_name","password1","password2")
    
class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name","last_name","bio","avatar","display_name","location","website")
    