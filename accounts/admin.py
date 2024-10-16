from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Tutor
from .forms import CustomUserCreationForm, CustomUserChangeForm


class TutorAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Tutor
    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "subjects",
        "availability",
    ]
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("subjects", "availability")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("subjects", "availability")}),
    )


admin.site.register(Tutor, TutorAdmin)
