from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Table


class IndexView(generic.ListView):
    model = Table
    template_name = 'tables/index.html'


class DetailView(generic.DetailView):
    model = Table
    template_name = 'tables/detail.html'
