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

    def __str__(self):
        published_on = self.published_on.strftime("%Y-%m-%d %H:%M")
        return f'Review published on {published_on} for {self.property.name}'

