from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cat


class CatListView(ListView):
    model = Cat

    # get all cats
    def get_queryset(self):
        return Cat.objects.all()


class CatDetailView(DetailView):
    model = Cat

    # get cat by id
    def get_object(self, queryset=None):
        return Cat.objects.get(id=self.kwargs['pk'])


class CatCreateView(CreateView):
    model = Cat
    fields = ['nickname', 'breed', 'weight']
    success_url = reverse_lazy('cats:cat_list')


class CatUpdateView(UpdateView):
    model = Cat
    fields = ['nickname', 'breed', 'weight']
    success_url = reverse_lazy('cats:cat_list')

class CatDeleteView(DeleteView):
    model = Cat
    success_url = reverse_lazy('cats:cat_list')
