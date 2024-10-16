from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Tutor


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Tutor
        fields = [
            "username",
            "password1",
            "password2",
            "email",
            "first_name",
            "last_name",
            "subjects",
        ]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Tutor
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "subjects",
            "availability",
        ]
        widgets = {
            "availability": forms.Textarea(attrs={"rows": 4, "cols": 40}),
        }
