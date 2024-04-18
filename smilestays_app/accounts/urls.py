from django.urls import path, include

from smilestays_app.accounts.views import SignUpView, SignInView, sign_out, DetailsProfileView, EditProfileView, \
    DeleteProfileView

urlpatterns = [
    path('register', SignUpView.as_view(), name='sign up'),
    path('login', SignInView.as_view(), name='sign in'),
    path('logout', sign_out, name='sign out'),
    path('<int:pk>/', include([
        path('details', DetailsProfileView.as_view(), name='details profile'),
        path('edit', EditProfileView.as_view(), name='edit profile'),
        path('delete', DeleteProfileView.as_view(), name='delete profile')
    ]))
]