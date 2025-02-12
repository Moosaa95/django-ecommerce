from django.urls import path, include
from . import views

urlpatterns = [
        
  path('', views.home, name='home'),
  
  # Category URLs
    path('categories/', views.list_categories, name='category_list'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/<int:category_id>/', views.retrieve_category, name='category_detail'),
    path('categories/<int:category_id>/update/', views.update_category, name='update_category'),
    path('categories/<int:category_id>/delete/', views.delete_category, name='delete_category'),
    
    # Product URLs
    path('products/', views.list_product, name='product_list'),
    path('products/create/', views.create_product, name='create_product'),
    path('products/<int:product_id>/', views.retrieve_product, name='product_detail'),
    path('products/<int:product_id>/update/', views.update_product, name='update_product'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    
]