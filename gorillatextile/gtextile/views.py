from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import User, Category, Product
from .forms import UserRegisterForm, CategoryForm, ProductForm
from django.db.models import Q

# Create your views here.
def home(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')

    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )

    if category_id:
        products = products.filter(category_id=category_id)

    categories = Category.objects.all()
    return render(request, "homepage.html", {
        "products": products,
        "categories": categories,
        "query": query,
        "selected_category": category_id
    })


@login_required
def seller_dashboard(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, "seller/seller_dashboard.html",{
        "products":products,
        "category":categories,
    })

@login_required
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = request.user
            product.save()
            # Handle multiple images if needed
            images = request.FILES.getlist('images')
            for img in images:
                product.images.create(image=img)
            return redirect("sellerd")  # Redirect to your product list page
    else:
        form = ProductForm()
         # If you want to pre-populate categories in the form (optional)
    categories = Category.objects.all()
    # You could pass categories to template if you use the form on dashboard page
    return redirect("sellerd")

@login_required
def category_create(request):
    if request.method == "POST":
        print("posted")
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new category
            return redirect("sellerd") # Redirect to your product list page

    else:
        form = CategoryForm()
         # If you want to pre-populate categories in the form (optional)
    categories = Category.objects.all()
    # You could pass categories to template if you use the form on dashboard page
    return redirect("sellerd")


@login_required
def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id, created_by=request.user)
    if request.method == "POST":
        product.name = request.POST.get("name")
        product.category_id = request.POST.get("category")
        product.description = request.POST.get("description")
        product.save()
        return redirect("sellerd")  # or seller dashboard page
    return redirect("sellerd")

@login_required
def add_product_image(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = get_object_or_404(Product, id=product_id)
        images = request.FILES.getlist("images")
        for img in images:
            product.images.create(image=img)
        return redirect("sellerd")  # Redirect back to your product table


@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect("sellerd")

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect("sellerd") 