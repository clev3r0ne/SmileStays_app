from django.urls import path

from smilestays_app.photos.views import AddPhotoView, DeletePhotoView

urlpatterns = [
    path('add', AddPhotoView.as_view(), name='add photo'),
    path('delete/<int:pk>', DeletePhotoView.as_view(), name='delete photo')
]