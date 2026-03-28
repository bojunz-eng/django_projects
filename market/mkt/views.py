from django.http import HttpResponse
from django.contrib.auth import get_user_model

from mkt.models import Ad
from mkt.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class AdListView(OwnerListView):
    model = Ad
    # By convention:
    # template_name = "mkt/ad_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad

class AdCreateView(OwnerCreateView):
    model = Ad
    # List Ad model fields to copy to the Ad form / template
    fields = ['title', 'price', 'text']

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']


class AdDeleteView(OwnerDeleteView):
    model = Ad

def change_user(request):
    '''
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
    ad = Ad(title="New Ad", text="Seeking Running Partner for Early Morning Runs", price=100, owner=user)
    ad.save()
    return HttpResponse(f"user password changed: {user.password}") 
