from django.views.generic import ListView, DetailView, TemplateView
from .models import Vesti


class VestiListView(ListView):
    model = Vesti
    context_object_name = "vesti"
    paginate_by = 3


class VestDetailView(DetailView):
    model = Vesti


class GalleryTemplateView(TemplateView):
    template_name = "vesti/gallery.html"
