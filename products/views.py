from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Product, Category
from .forms import ProductForm


def all_categories(request):
    """
    Renders all books
    """

    categories = Category.objects.all()

    context = {
        'categories': categories,
    }

    return render(request, 'products/categories.html', context)


def products(request):
    """
    Renders all products of same category
    """
    products = Product.objects.all()
    category_select = request.GET['category']

    if request.GET:
        if 'category' in request.GET:
            category_select = request.GET['category']
            products = products.filter(category__name=category_select)

    context = {
        'products': products,
        'current_category': category_select,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    
    """
    Displays product details
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)

