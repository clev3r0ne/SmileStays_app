from django.contrib import admin

from smilestays_app.photos.models import PropertyPhoto


@admin.register(PropertyPhoto)
class PropertyPhotoAdmin(admin.ModelAdmin):
    pass
