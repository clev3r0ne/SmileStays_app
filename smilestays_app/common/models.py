from django.core.validators import MinLengthValidator
from django.db import models

from smilestays_app.properties.models import Property


class Review(models.Model):

    text = models.TextField(
        max_length=500,
    )

    published_on = models.DateTimeField(
        auto_now_add=True,
        blank = True,
        null = False,
    )

    property = models.ForeignKey(
        Property, on_delete=models.CASCADE
    )

    #TO DO: profile = models.ForeignKey()

