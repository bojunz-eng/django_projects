
from django.conf import settings
from django.http import HttpResponse


def home(request):
    # display installed apps
    return HttpResponse("""
    <h1>Welcome to MySite</h1>
    <p>Installed apps:</p>
    <ul>
        <li><a href="admin">admin</a></li>
        <li><a href="polls">polls</a></li>
    </ul>
    """)
    