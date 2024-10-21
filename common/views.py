from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import  BaseFormView

from MyMusicApp.utils import get_user_obj
from albums.models import Album
from profiles.forms import ProfileCreateForm

# function base view - 1 if

class HomePage(ListView, BaseFormView): # списъци и форми
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None,**kwargs):
        context = super().get_context_data()
        context['profile'] = get_user_obj()
        return context

    def get_template_names(self):
        profile = get_user_obj() # None or QuerySet

        if profile:
            return ['profiles/home-with-profile.html']

        return ['profiles/home-no-profile.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)