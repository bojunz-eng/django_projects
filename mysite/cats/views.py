from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cat


class CatList(LoginRequiredMixin, ListView):
    model = Cat

    # get all cats
    def get_queryset(self):
        return Cat.objects.all()


class CatDetail(LoginRequiredMixin, DetailView):
    model = Cat

    # get cat by id
    def get_object(self, queryset=None):
        return Cat.objects.get(id=self.kwargs['pk'])


class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = ['nickname', 'breed', 'weight', 'foods']
    success_url = reverse_lazy('cats:all')


class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = ['nickname', 'breed', 'weight']
    success_url = reverse_lazy('cats:all')


class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    success_url = reverse_lazy('cats:all')
