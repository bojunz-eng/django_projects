from django.urls import path
from . import views

app_name = "cats"
urlpatterns = [
    path('', views.CatList.as_view(), name='all'),
    path('main/<int:pk>/', views.CatDetail.as_view(), name='cat_detail'),
    path('main/create/', views.CatCreate.as_view(), name='cat_create'),
    path('main/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('main/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
]
