from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Flavor
from django.urls import reverse_lazy

# Create your views here.

class HomePageView(ListView):
    template_name = 'home.html'
    model = Flavor
    context_object_name = 'all_flavors'

class FlavorDetailView(DetailView):
    template_name = 'flavors_details.html'
    model = Flavor

class FlavorCreateView(CreateView):
    template_name = 'flavors_new.html'
    model = Flavor
    fields = ['name', 'description', 'author']

class FlavorUpdateView(UpdateView):
    template_name = 'flavors_update.html'
    model = Flavor
    fields = ['name', 'description']

class FlavorDeleteView(DeleteView):
    template_name = 'flavors_delete.html'
    model = Flavor
    fields = ['name']
    success_url = reverse_lazy('home')