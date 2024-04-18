from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from smilestays_app.accounts.models import Profile

UserModel = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'profile_pic')

    def save(self, commit=True):
        user = super().save(commit=commit)
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        profile_pic = self.cleaned_data['profile_pic']

        profile = Profile(
            user=user,
            first_name=first_name,
            last_name=last_name,
            profile_pic=profile_pic
        )

        if commit:
            profile.save()

        return user

