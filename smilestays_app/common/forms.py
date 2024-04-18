from django import forms

from smilestays_app.common.models import Review


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'property', 'user']
        widgets = {
            'text': forms.Textarea(attrs={
                'style' : "width:580px; height:150px;",
            }),
        }



class DeleteReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ()
