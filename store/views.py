from django.shortcuts import render
from store.models import Product, Order

# Create your views here.

def index(request):
    context = {}
    return render(request, 'store/index.html', context)

def inventory(request):
    product_list = Product.objects.order_by("product_id")
    context = {"product_list" : product_list}
    return render(request, 'store/inventory.html', context)

def basket(request):
    context = {}
    return render(request, 'store/basket.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)

def product(request, product_id):
    product = Product.objects.get(product_id=product_id)
    context = {"product" : product}
    return render(request, 'store/product.html', context)