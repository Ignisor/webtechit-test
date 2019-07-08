from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from python_test.forms import SearchForm
from python_test.models import Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('name', 'email', 'phone')
    template_name = 'client_form.html'
    success_url = reverse_lazy('client-list')


class ClientUpdateView(UpdateView):
    model = Client
    fields = '__all__'
    template_name = 'client_form.html'
    success_url = reverse_lazy('client-list')


class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        ctx['search_form'] = SearchForm()
        ctx['order_fields'] = SearchForm.base_fields.keys()

        return ctx

    def get_queryset(self):
        query = super().get_queryset()
        filters = {
            key + '__icontains': self.request.GET.get(key, '')
            for key in SearchForm.base_fields.keys()
            if self.request.GET.get(key, '')
        }

        query = query.filter(**filters)

        ordering = self.request.GET.get('order_by', None)
        if ordering:
            query = query.order_by(ordering)

        return query
