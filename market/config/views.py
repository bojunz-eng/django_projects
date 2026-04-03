from django.http import HttpResponse
from django.views import View
from django.contrib.auth import get_user_model

def profile(request):
    # get user id
    user_id = request.user.id
    # get user info
    User = get_user_model()
    user = User.objects.get(id=user_id)
    # get user profile
    profile = str(user)
    return HttpResponse(profile)
