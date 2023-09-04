from django.shortcuts import render
from store.models import Product, Order
from django.http import JsonResponse
import json
from .models import * 


def index(request):
    product_list = Product.objects.order_by("product_id")
    context = {"product_list" : product_list}
    return render(request, 'store/index.html', context)

def basket(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items - [] 
        order = {'get_basket_total':0, 'get_basket_items':0}   
    context = {'items' : items, 'order' : order}
    return render(request, 'store/basket.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items - [] 
        order = {'get_basket_total':0, 'get_basket_items':0}   

    context = {'items' : items, 'order' : order}
    return render(request, 'store/checkout.html', context)

def product(request, product_id):
    product = Product.objects.get(product_id=product_id)
    context = {"product" : product}
    return render(request, 'store/product.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action: ', action)
    print('ProductId: ', productId)

    customer = request.user.customer
    product = Product.objects.get(product_id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)