from django.urls import path

from . import views

app_name = "solo2"

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
]

