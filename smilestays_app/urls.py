from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = ([
    path('admin/', admin.site.urls),
    path('', include('smilestays_app.common.urls')),
    path('properties/', include('smilestays_app.properties.urls')),
    path('photos/', include('smilestays_app.photos.urls'))
]) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
