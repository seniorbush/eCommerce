from django.shortcuts import render
from store.models import Product, Order
from django.http import JsonResponse
import json
import datetime
from .models import * 


def index(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        basketItems = order.get_basket_items
    else:
        items - [] 
        order = {'get_basket_total':0, 'get_basket_items':0}
        basketItems = order['get_basket_total']

    product_list = Product.objects.order_by("product_id")
    context = {"product_list" : product_list, "basketItems" : basketItems}
    return render(request, 'store/index.html', context)

def basket(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        basketItems = order.get_basket_items
    else:
        items - [] 
        order = {'get_basket_total':0, 'get_basket_items':0}  
        basketItems = order['get_basket_total'] 
    context = {'items' : items, 'order' : order, "basketItems" : basketItems}
    return render(request, 'store/basket.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        basketItems = order.get_basket_items
    else:
        items - [] 
        order = {'get_basket_total':0, 'get_basket_items':0}   
        basketItems = order['get_basket_total'] 
    context = {'items' : items, 'order' : order, "basketItems" : basketItems}
    return render(request, 'store/checkout.html', context)

def product(request, product_id):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        basketItems = order.get_basket_items
    else:
        items - [] 
        order = {'get_basket_total':0, 'get_basket_items':0}   
        basketItems = order['get_basket_total'] 
    product = Product.objects.get(product_id=product_id)
    context = {"product" : product, "basketItems" : basketItems}
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

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_basket_total:
            order.complete = True

            ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['form']['addressLine'], 
            city=data['form']['townCity'],
            postcode=data['form']['postcode'])

        order.save()
      
    else:
        print('User not logged in')
    return JsonResponse('Payment Complete', safe=False)

