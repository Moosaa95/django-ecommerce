from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth import authenticate , login 
from django.contrib import messages
from django.contrib.auth.models import User
from .models import product
from .forms import ProductForm
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

# Create your views here.
def create_product(request):
    
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            
            product = product.create_product(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data.get('image')
            )
            return redirect('product_list') 
    else:
        form = ProductForm()

    return render(request, 'create_product.html', {'form': form})


def update_product(request, product_id):
    
    product = get_object_or_404(product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            a
            updated_product = product.update_product(
                product_id=product.id,
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data.get('image')
            )
            return redirect('product_detail', product_id=updated_product.id)  
    else:
        form = ProductForm(instance=product)

    return render(request, 'update_product.html', {'form': form, 'product': product})


def list_product(request):
    
    product = product.list_product() 
    return render(request, 'product_list.html', {'Product': product})


def retrieve_product(request, product_id):
    
    product = get_object_or_404(product, id=product_id)  
    return render(request, 'product_detail.html', {'product': product})


def delete_product(request, product_id):
   
    success = product.delete_product(product_id)  
    if success:
        return redirect('product_list') 
    else:
        return JsonResponse({'error': 'Product not found'}, status=404)  


def register(request):
  form = SignUpForm()
  if request.method == "POST":
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.clean_data['username']
      password = form.clean_data['password1']
      #login user
      user = authenticate(username=username, password=password)
      login(request,user)
      messages.sucess(request, ("whoops! something went wrong, please try again..."))
      return redirect('register')
     
  return render(request, 'register.html', {'form':form})
  
