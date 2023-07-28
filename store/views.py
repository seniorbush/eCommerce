from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'store/index.html', context)

def inventory(request):
    context = {}
    return render(request, 'store/inventory.html', context)

def basket(request):
    context = {}
    return render(request, 'store/basket.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)