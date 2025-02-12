from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Category, Product
from .forms import CategoryForm, ProductForm, SignUpForm  # Ensure SignUpForm is imported

def home(request):
    context = {
        "featured_products": range(4),  # Placeholder for featured products
        "all_products": range(8),      # Placeholder for all products
        "testimonials": range(3),      # Placeholder for testimonials
        "categories": range(3),        # Placeholder for categories
    }
    return render(request, "home.html", context)

# View to create a new category
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            Category.create_category(**form.cleaned_data)
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})

# View to create a new product
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            Product.create_product(**form.cleaned_data)
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})

# View to update an existing category
def update_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            Category.update_category(category_id=category.id, **form.cleaned_data)
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'update_category.html', {'form': form, 'category': category})

# View to update an existing product
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            Product.update_product(product_id=product.id, **form.cleaned_data)
            return redirect('product_detail', product_id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form, 'product': product})

# View to list all categories
def list_categories(request):
    categories = Category.list_categories()
    return render(request, 'categories_list.html', {'categories': categories})

# View to retrieve and display a single category
def retrieve_category(request, category_id):
    category = Category.get_category_by_id(category_id)
    return render(request, 'category_detail.html', {'category': category})

# View to delete a category
def delete_category(request, category_id):
    success = Category.delete_category(category_id)
    if success:
        return redirect('category_list')
    return JsonResponse({'error': 'Category not found'}, status=404)

# View to list all products
def list_product(request):
    products = Product.list_products()
    return render(request, 'product_list.html', {'products': products})

# View to retrieve and display a single product
def retrieve_product(request, product_id):
    product = Product.get_product_by_id(product_id)
    return render(request, 'product_detail.html', {'product': product})

# View to delete a product
def delete_product(request, product_id):
    success = Product.delete_product(product_id)
    if success:
        return redirect('product_list')
    return JsonResponse({'error': 'Product not found'}, status=404)

# User registration view
def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Authentication failed. Please try again.")
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
