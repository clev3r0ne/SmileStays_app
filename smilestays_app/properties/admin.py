from django.contrib import admin

from smilestays_app.properties.models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    pass
