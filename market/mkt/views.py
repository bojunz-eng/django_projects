from django.http import HttpResponse
from django.contrib.auth import get_user_model

from mkt.models import Ad, Comment
from mkt.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from mkt.forms import CreateForm, CommentForm

class AdListView(OwnerListView):
    model = Ad
    # By convention:
    # template_name = "mkt/ad_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = "mkt/ad_detail.html"
    
    def get(self, request, pk) :
        x = get_object_or_404(Ad, id=pk)
        comments = Comment.objects.filter(ad=x).order_by('-updated_at')
        comment_form = CommentForm()
        context = { 'ad' : x, 'comments': comments, 'comment_form': comment_form }
        return render(request, self.template_name, context)

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


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        f = get_object_or_404(Ad, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, ad=f)
        comment.save()
        return redirect(reverse('mkt:ad_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "mkt/comment_delete.html"

    # https://stackoverflow.com/questions/26290415/deleteview-with-a-dynamic-success-url-dependent-on-id
    def get_success_url(self):
        ad = self.object.ad
        return reverse('mkt:ad_detail', args=[ad.id])


def change_user(request):
    '''
    dj4e_user1 (copy) / Meow_16751b_41 (copy)
    dj4e_user2 (copy) / Meow_42_16751b (copy)

    dj4e_user1 (copy) / Meow_782113_41 (copy)
    dj4e_user2 (copy) / Meow_42_782113 (copy)
    
    Spanish Lessons Available: Beginner to Advanced Levels
    Seeking Running Partner for Early Morning Runs
    '''

    password1, password2, title = get_info(2)
    
    # change user password
    User = get_user_model()
    user = User.objects.get(username="dj4e_user1")
    user.set_password(password1)
    user.save()

    user = User.objects.get(username="dj4e_user2")
    user.set_password(password2)
    user.save()
    
    # Add a new Ad
    ad = Ad(title=title, text=title, price=100, owner=user)
    ad.save()
    return HttpResponse(f"dj4e_user1 password: {password1}<br>dj4e_user2 password: {password2} <br>title: {title}") 

def get_info(version):
    if version == "1":
        return "Meow_16751b_41", "Meow_42_16751b", "Spanish Lessons Available: Beginner to Advanced Levels"
    else:
        return "Meow_782113_41", "Meow_42_782113", "Seeking Running Partner for Early Morning Runs"

def stream_file(request, pk):
    ad = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = ad.content_type
    response['Content-Length'] = len(ad.picture)
    response.write(ad.picture)
    return response
