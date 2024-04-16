from django.core.validators import MinLengthValidator
from django.db import models

from smilestays_app.common.validators import validate_starts_with_uppercase


class Property(models.Model):
    CHOICES = (
        ('Hotel', 'Hotel'),
        ('Apartment', 'Apartment'),
        ('Resort', 'Resort'),
        ('Villa', 'Villa'),
        ('Guest house', 'Guest house'),
        ('Hostel', 'Hostel')
    )
    MAX_LENGTH_CHOICES = max([len(x[0]) for x in CHOICES])

    name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(5), validate_starts_with_uppercase]
    )

    description = models.TextField(
        max_length=500,
        validators=[MinLengthValidator(20)]
    )

    location = models.CharField(
        max_length=50
    )

    address = models.CharField(
        max_length=50
    )

    phone_number = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(10)]
    )

    cover_photo = models.ImageField(
        upload_to='cover_photos'
    )

    listed_on = models.DateTimeField(
        auto_now_add=True,
        blank = True,
        null = False
    )

    category = models.CharField(
        max_length=MAX_LENGTH_CHOICES,
        choices=CHOICES
    )

    price_for_room_per_night = models.IntegerField()


    #TO DO: profile = models.ForeignKey()