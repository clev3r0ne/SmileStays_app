from django.urls import path, include

from smilestays_app.common.views import HomeView, MyPropertiesView, DeleteReviewView

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('my_properties/', MyPropertiesView.as_view(), name='my properties'),
    path('<int:pk>/', include([
        # path('add_review/', AddReviewView.as_view(), name='add review'),
        path('delete_review/', DeleteReviewView.as_view(), name='delete review')
    ]))
]