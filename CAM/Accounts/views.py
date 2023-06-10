from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.


def home(request):
    orders = Order.objects.all()
    customer = Customer.objects.all()
    context = {'orders':orders,'customer':customer}

    return render(request, 'Accounts/dashboard.html',context)

def products(request):
    products = Product.objects.all()
    return render(request, 'Accounts/products.html',{'products':products})

def customer(request):
    return render(request,'Accounts/customer.html')


