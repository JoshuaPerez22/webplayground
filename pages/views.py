from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin # Utilizado en PageCreate
from .models import Page
from .forms import PageForm

# Create your views here.

# Esta es una forma de hacer el mixin de autenticación, utilizado en PageUpdate y PageDelete
class StaffRequiredMixin(object):
    """
    Este Mixin requerirá autenticación del usuario
    """
    def dispatch(self, request, *args, **kargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kargs)


class PageListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page


class PageCreate(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')
    login_url = reverse_lazy('admin:login')


class PageUpdate(StaffRequiredMixin, UpdateView):
    model = Page
    form_clasws = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


class PageDelete(StaffRequiredMixin, DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
