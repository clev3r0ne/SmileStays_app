from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from smilestays_app.photos.forms import AddPhotoForm, DeletePhotoForm
from smilestays_app.photos.models import PropertyPhoto
from smilestays_app.properties.models import Property


class AddPhotoView(CreateView):
    Model = PropertyPhoto
    template_name = 'photos/add-photo.html'
    form_class = AddPhotoForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class=AddPhotoForm)
        property_id = self.request.GET.get('property_id')
        form.instance.property = Property.objects.all().get(pk=property_id)

        return form

    def get_success_url(self):
        property_id = self.request.GET.get('property_id')
        return reverse_lazy('details property', kwargs={'pk': property_id})


class DeletePhotoView(DeleteView):
    model = PropertyPhoto
    template_name = 'photos/delete-photo.html'
    form_class = DeletePhotoForm

    def get_success_url(self):
        property_id = self.request.GET.get('property_id')
        return reverse_lazy('details property', kwargs={'pk': property_id})
