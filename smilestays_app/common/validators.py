from django.core.exceptions import ValidationError


def validate_starts_with_uppercase(value):
    if value[0].islower():
        raise ValidationError('Name must start with uppercase')