from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Tutor(AbstractUser):
    subjects = models.CharField(max_length=100)
    availability = models.JSONField(default=dict, blank=True, null=True)

    def __str__(self):
        return self.username
