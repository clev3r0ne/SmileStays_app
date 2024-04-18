from django import forms

from smilestays_app.properties.models import Property


class AddPropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ['user']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control border-success",
                'style': 'max-width: 300px;',
                'placeholder': 'Name of the property'
            }),
            'description': forms.Textarea(attrs={
                'class': "form-control border-success",
                'style': 'max-height: 500px; max-width: 400px;',
                'placeholder': 'Please describe your property in a few words...'
            }),
            'location': forms.TextInput(attrs={
                'class': "form-control border-success",
                'style': 'max-width: 300px;',
                'placeholder': 'Town/City'
            }),
            'address': forms.TextInput(attrs={
                'class': "form-control border-success",
                'style': 'max-width: 300px;',
                'placeholder': 'Address of the property'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': "form-control border-success",
                'style': 'max-width: 300px;',
                'placeholder': 'Phone number'
            }),
            'category': forms.Select(attrs={
                'class': "form-control border-success",
                'style': 'max-width: 300px;',
                'placeholder': 'Category of the property'
            }),
            'price_for_room_per_night': forms.NumberInput(attrs={
                'class': "form-control border-success",
                'style': 'max-width: 300px;',
                'placeholder': 'Price in USD($)'
            }),
            'user': forms.HiddenInput(),
        }




class EditPropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'


class DeletePropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ()
