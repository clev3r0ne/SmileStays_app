from django.urls import path, include

from smilestays_app.properties.views import AddPropertyView, DetailsPropertyView, EditPropertyView, DeletePropertyView

urlpatterns = [
    path('add/', AddPropertyView.as_view(), name='add property'),
    path('<int:pk>/', include([
        path('details/', DetailsPropertyView.as_view(), name='details property'),
        path('edit/', EditPropertyView.as_view(), name='edit property'),
        path('delete/', DeletePropertyView.as_view(), name='delete property')
    ]))
]