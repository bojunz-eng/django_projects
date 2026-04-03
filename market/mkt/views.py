from django.http import HttpResponse
from django.contrib.auth import get_user_model

from mkt.models import Ad
from mkt.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from mkt.forms import CreateForm

class AdListView(OwnerListView):
    model = Ad
    # By convention:
    # template_name = "mkt/ad_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad

'''
class AdCreateView(OwnerCreateView):
    model = Ad
    # List Ad model fields to copy to the Ad form / template
    fields = ['title', 'price', 'text']

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']
'''

class AdCreateView(LoginRequiredMixin, View):
    template_name = 'mkt/ad_form.html'
    success_url = reverse_lazy('mkt:all')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)


class AdUpdateView(LoginRequiredMixin, View):
    template_name = 'mkt/ad_form.html'
    success_url = reverse_lazy('mkt:all')

    def get(self, request, pk):
        pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(instance=pic)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
        form = CreateForm(request.POST, request.FILES or None, instance=pic)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        pic = form.save(commit=False)
        pic.save()

        return redirect(self.success_url)


class AdDeleteView(OwnerDeleteView):
    model = Ad

def change_user(request):
    '''
    
    dj4e_user1 (copy) / Meow_16751b_41 (copy)
    dj4e_user2 (copy) / Meow_42_16751b (copy)

    dj4e_user1 (copy) / Meow_782113_41 (copy)
    dj4e_user2 (copy) / Meow_42_782113 (copy)
    '''

    # change user password
    User = get_user_model()
    user = User.objects.get(username="dj4e_user1")
    user.set_password("Meow_782113_41")
    user.save()

    user = User.objects.get(username="dj4e_user2")
    user.set_password("Meow_42_782113")
    user.save()
    
    # Add a new Ad
    ad = Ad(title="Seeking Running Partner for Early Morning Runs", text="Seeking Running Partner for Early Morning Runs", price=100, owner=user)
    ad.save()
    return HttpResponse(f"user password changed: {user.password}") 

def stream_file(request, pk):
    pic = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response
