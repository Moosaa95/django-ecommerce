from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Category
from .forms import CategoryForm  # Assuming you have a CategoryForm for handling form submissions


def home(request):
    context = {
        "featured_products": range(4),  # For featured products
        "all_products": range(8),      # For all products
        "testimonials": range(3),      # For testimonials
        "categories": range(3),      # For testimonials
    }
    return render(request, "home.html", context)


# View to create a new category
def create_category(request):
    """
    Handles the creation of a new category. If the request is a POST request, it processes the form.
    If successful, it redirects to the category list page. Otherwise, it renders the form again.
    """
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            # Create the category using the form data
            category = Category.create_category(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data.get('image')
            )
            return redirect('category_list')  # Redirect to the category list view
    else:
        form = CategoryForm()

    return render(request, 'create_category.html', {'form': form})

# View to update an existing category
def update_category(request, category_id):
    """
    Handles the updating of an existing category. If the request is a POST request, it processes the form.
    If successful, it redirects to the category detail page. Otherwise, it renders the form again.
    """
    category = get_object_or_404(Category, id=category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            # Update the category using the form data
            updated_category = Category.update_category(
                category_id=category.id,
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data.get('image')
            )
            return redirect('category_detail', category_id=updated_category.id)  # Redirect to the category detail view
    else:
        form = CategoryForm(instance=category)

    return render(request, 'update_category.html', {'form': form, 'category': category})

# View to list all categories
def list_categories(request):
    """
    Displays a list of all categories.
    """
    categories = Category.list_categories()  # Retrieve all categories
    return render(request, 'categories_list.html', {'categories': categories})

# View to retrieve and display a single category
def retrieve_category(request, category_id):
    """
    Displays the details of a single category.
    """
    category = get_object_or_404(Category, id=category_id)  # Retrieve the category by ID
    return render(request, 'category_detail.html', {'category': category})

# View to delete a category
def delete_category(request, category_id):
    """
    Deletes a category and redirects to the category list page.
    """
    success = Category.delete_category(category_id)  # Delete the category by ID
    if success:
        return redirect('category_list')  # Redirect to the category list view
    else:
        return JsonResponse({'error': 'Category not found'}, status=404)  # Return error if category does not exist
