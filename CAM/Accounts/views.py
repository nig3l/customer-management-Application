from django.shortcuts import render
from django.http import HttpResponse
from  .models import *

# Create your views here.


def home(request):
    orders = Order.objects.all()
    customer = Customer.objects.all()

    total_customers = customer.count()
    total_orders = orders.count()
    delivered = orders.filter(status = 'deliverd').count()
    pending = orders.filter(status = 'pending').count()

    context = {'orders':orders,'customer':customer,'total_customers':total_customers,
                'total_orders':total_orders,'delivered':delivered,'pending':pending}

    return render(request, 'Accounts/dashboard.html',context)

def products(request):
    products = Product.objects.all()
    return render(request, 'Accounts/products.html',{'products':products})

def customer(request):
    # customer = Customer.objects.all()
    return render(request,'Accounts/customer.html')



