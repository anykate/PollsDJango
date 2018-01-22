from django.shortcuts import render
from django.views.generic import ListView
from .models import Poll


# Create your views here.
class IndexPageView(ListView):
    model = Poll
    template_name = 'polls/index.html'
