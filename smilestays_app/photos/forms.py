from django import forms

from smilestays_app.photos.models import PropertyPhoto


class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = PropertyPhoto
        fields = ('image',)


class DeletePhotoForm(forms.ModelForm):
    class Meta:
        model = PropertyPhoto
        fields = ()
