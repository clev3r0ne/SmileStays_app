from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    profile_pic = models.ImageField(
        upload_to='profile_pics',
        blank=True,
        null=True,
        verbose_name="Profile Picture"
    )

    user = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE
    )
