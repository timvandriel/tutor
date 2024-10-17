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


class UpdateAvailabilityForm(forms.ModelForm):
    DAYS_OF_WEEK = [
        ("monday", "Monday"),
        ("tuesday", "Tuesday"),
        ("wednesday", "Wednesday"),
        ("thursday", "Thursday"),
        ("friday", "Friday"),
        ("saturday", "Saturday"),
        ("sunday", "Sunday"),
    ]

    available_days = forms.MultipleChoiceField(
        choices=DAYS_OF_WEEK,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Select the days you are available",
    )
    monday_hours = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "e.g., 9:00-11:00, 14:00-16:00"}),
    )
    tuesday_hours = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "e.g., 9:00-11:00, 14:00-16:00"}),
    )
    wednesday_hours = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "e.g., 9:00-11:00, 14:00-16:00"}),
    )
    thursday_hours = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "e.g., 9:00-11:00, 14:00-16:00"}),
    )
    friday_hours = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "e.g., 9:00-11:00, 14:00-16:00"}),
    )
    saturday_hours = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "e.g., 9:00-11:00, 14:00-16:00"}),
    )
    sunday_hours = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "e.g., 9:00-11:00, 14:00-16:00"}),
    )
    subjects = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "List the subjects you can tutor"}),
        required=False,
    )

    class Meta:
        model = Tutor
        fields = [
            "available_days",
            "monday_hours",
            "tuesday_hours",
            "wednesday_hours",
            "thursday_hours",
            "friday_hours",
            "saturday_hours",
            "sunday_hours",
            "subjects",
        ]
