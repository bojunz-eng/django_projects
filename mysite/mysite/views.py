
from django.conf import settings
from django.http import HttpResponse


def all_apps(request):
    # display installed apps
    return HttpResponse("""
    <h1>Welcome to MySite</h1>
    <p>Installed apps:</p>
    <ul>
        <li><a href="admin">admin</a></li>
        <li><a href="polls">polls</a></li>
        <li><a href="solo1">solo1</a></li>
        <li><a href="hello">hello</a></li>
        <li><a href="cats">cats</a></li>
    </ul>
    """)
    