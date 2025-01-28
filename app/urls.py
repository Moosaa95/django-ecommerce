from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('categories/', views.list_categories, name='category_list'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/<int:category_id>/', views.retrieve_category, name='category_detail'),
    path('categories/<int:category_id>/update/', views.update_category, name='update_category'),
    path('categories/<int:category_id>/delete/', views.delete_category, name='delete_category'),
]

