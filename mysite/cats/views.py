from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cat, Breed

'''
class CatList(LoginRequiredMixin, View):
    def get(self, request):
        bc = Breed.objects.count()
        cl = Cat.objects.all()

        ctx = {'breed_count': bc, 'cat_list': cl}
        return render(request, 'cats/cat_list.html', ctx)
'''
class CatList(LoginRequiredMixin, ListView):
    model = Cat

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['breed_count'] = Breed.objects.count()
        return context
    
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

class BreedList (LoginRequiredMixin, ListView):
    model = Breed
    
    
class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = ['name']
    success_url = reverse_lazy('cats:all')
    
class BreedDetail(LoginRequiredMixin, DetailView):
    model = Breed
    
    def get_object(self, queryset=None):
        return Breed.objects.get(id=self.kwargs['pk'])
    
class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = ['name']
    success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    success_url = reverse_lazy('cats:all')
    