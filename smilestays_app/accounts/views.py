from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from smilestays_app.accounts.forms import SignUpForm
from smilestays_app.accounts.models import Profile
from smilestays_app.common.mixins import IfNotOwnerRedirectMixin

from smilestays_app.properties.models import Property


class SignUpView(CreateView):
    template_name = "accounts/sign-up.html"
    form_class = SignUpForm
    success_url = reverse_lazy("index")

    def get(self, request, *args, **kwargs):
        result = super().get(request, *args, **kwargs)

        if request.user.is_authenticated:
            return redirect('index')

        return result


    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)

        return result



class SignInView(LoginView):
    template_name = "accounts/sign-in.html"
    redirect_authenticated_user = True


def sign_out(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('index')


class DetailsProfileView(IfNotOwnerRedirectMixin, DetailView):
    template_name = "accounts/details-profile.html"

    queryset = Profile.objects.all().select_related('user')


class EditProfileView(IfNotOwnerRedirectMixin, UpdateView):
    queryset = Profile.objects.all().select_related('user')
    template_name = 'accounts/edit-profile.html'
    fields = ['first_name', 'last_name', 'profile_pic',]

    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={'pk': self.object.pk})


class DeleteProfileView(IfNotOwnerRedirectMixin, DeleteView):
    queryset = Profile.objects.all()
    template_name = 'accounts/delete-profile.html'
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        profile = self.get_object()
        profile.user.delete()
        profile.delete()
        logout(self.request)

        return redirect('index')

