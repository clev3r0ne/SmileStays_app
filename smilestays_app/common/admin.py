from django.contrib import admin

from smilestays_app.common.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass