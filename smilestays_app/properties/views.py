from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.edit import FormMixin

from smilestays_app.common.forms import AddReviewForm
from smilestays_app.common.mixins import IfNotOwnerRedirectMixin
from smilestays_app.common.models import Review
from smilestays_app.properties.forms import AddPropertyForm, EditPropertyForm, DeletePropertyForm
from smilestays_app.properties.models import Property


class AddPropertyView(CreateView):
    form_class = AddPropertyForm
    template_name = 'properties/add-property.html'

    def get_success_url(self):
        return reverse('details property', kwargs={'pk': self.object.pk})




class EditPropertyView(IfNotOwnerRedirectMixin, UpdateView):
    model = Property
    form_class = EditPropertyForm
    template_name = 'properties/edit-property.html'

    def get_success_url(self):
        return reverse_lazy('details property', kwargs={'pk': self.object.pk})


class DeletePropertyView(IfNotOwnerRedirectMixin, DeleteView):
    model = Property
    form_class = DeletePropertyForm
    template_name = 'properties/delete-property.html'

    def get_success_url(self):
        return reverse_lazy('my properties')


class DetailsPropertyView(LoginRequiredMixin, FormMixin, DetailView):
    context_object_name = 'current_property'
    # model = Property
    template_name = 'properties/details-property.html'
    form_class = AddReviewForm

    queryset = Property.objects.all() \
                .prefetch_related('propertyphoto_set') \
                .prefetch_related(Prefetch('review_set', queryset=Review.objects.prefetch_related('user__profile').order_by('-published_on')))

    def get_success_url(self):
        return reverse_lazy('details property', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddReviewForm(initial={'property': self.object, 'user': self.request.user})
        # context['reviews'] = Review.objects.all().select_related('user')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
