from django.urls import path
from . import views

app_name = "cats"
urlpatterns = [
    path('', views.CatListView.as_view(), name='cat_list'),
    path('<int:pk>/', views.CatDetailView.as_view(), name='cat_detail'),
    path('create/', views.CatCreateView.as_view(), name='cat_create'),
    path('update/<int:pk>/', views.CatUpdateView.as_view(), name='cat_update'),
    path('delete/<int:pk>/', views.CatDeleteView.as_view(), name='cat_delete'),
]
