from django.urls import path, include
from . import views

urlpatterns = [
         
  path('register/', views.register, name='register'),
  path('product/', views.list_product, name='product_list'),
  path('product/create/', views.create_product, name='create_product'),
  path('product/<int:product_id>/', views.retrieve_product, name='product_detail'),
  path('product/<int:product_id>/update/', views.update_product, name='update_product'),
  path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'), 
]