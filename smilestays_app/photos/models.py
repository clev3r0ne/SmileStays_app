from django.db import models

from smilestays_app.properties.models import Property


class PropertyPhoto(models.Model):

    image = models.ImageField(
        upload_to='property_photos'
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False
    )

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE
    )

    def __str__(self):
        created_on = self.created_on.strftime("%Y-%m-%d %H:%M")
        return f'{self.property.name} photo - {created_on}'
