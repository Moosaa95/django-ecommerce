from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login 
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

# Create your views here.

def home(request):
  return HttpResponse('')

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
    else: 
      return render(request, 'register.html', {'form':form})
  
