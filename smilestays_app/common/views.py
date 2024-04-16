from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView

from smilestays_app.common.forms import DeleteReviewForm
from smilestays_app.common.models import Review
from smilestays_app.properties.models import Property


class HomeView(ListView):
    context_object_name = 'properties'
    template_name = 'common/index.html'
    model = Property

    @property
    def get_category(self):
        return self.request.GET.get('category')

    @property
    def get_search_name_pattern(self):
        return self.request.GET.get('search_name_pattern')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_category
        search_name_pattern = self.get_search_name_pattern
        context['search_name_pattern'] = search_name_pattern or ''

        if search_name_pattern:
            context['properties'] = Property.objects.all().filter(name__icontains=search_name_pattern.lower()).order_by('listed_on')

        elif category:
            context['properties'] = Property.objects.all().filter(category=category).order_by('listed_on')

        return context


class MyPropertiesView(ListView):
    context_object_name = 'properties'
    template_name = 'common/my-properties.html'
    model = Property



class DeleteReviewView(DeleteView):
    model = Review
    # http_method_names = ['delete']


    # def dispatch(self, request, *args, **kwargs):
    #     # # safety checks go here ex: is user allowed to delete?
    #     # if request.user.username != kwargs['username']:
    #     #     return HttpResponseForbidden()
    #     # else:
    #         handler = getattr(self, 'delete')
    #         return handler(request, *args, **kwargs)

    def get_form(self, form_class=None):
        review_delete_form = super().get_form(form_class=DeleteReviewForm)
        return review_delete_form

    def get_success_url(self):
        # success_url = reverse_lazy('details property', kwargs={'pk': self.property_id})
        return reverse_lazy('index')


