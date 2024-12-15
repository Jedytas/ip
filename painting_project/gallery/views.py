from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Artist, Painting, Gallery
from .forms import ArtistForm, PaintingForm


# Views
class PaintingListView(ListView):
    model = Painting
    template_name = 'painting_list.html'
    context_object_name = 'paintings'

class PaintingDetailView(DetailView):
    model = Painting
    template_name = 'painting_detail.html'

class PaintingCreateView(CreateView):
    model = Painting
    form_class = PaintingForm
    template_name = 'painting_form.html'
    success_url = reverse_lazy('painting-list')

class PaintingUpdateView(UpdateView):
    model = Painting
    form_class = PaintingForm
    template_name = 'painting_form.html'
    success_url = reverse_lazy('painting-list')

class PaintingCreateView(CreateView):
    model = Painting
    form_class = PaintingForm
    template_name = 'gallery_form.html'
    success_url = reverse_lazy('painting-list')
