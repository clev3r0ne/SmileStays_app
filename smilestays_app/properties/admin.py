from django.contrib import admin

from smilestays_app.properties.models import Property


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'phone_number', 'listed_on']
    search_fields = ['name', 'location', 'phone_number']
