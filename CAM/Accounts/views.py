from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from  .models import *
from .forms import OrderForm
from .filters import OrderFilter

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

def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs


    context = {'customer':customer,'orders':orders,'order_count':order_count,'myFilter':myFilter}
    return render(request,'Accounts/customer.html',context)

def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product','status'),extra=10)

    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset= Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        # form = OrderForm(request.POST)
        # print('Printing POST',request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    
    context = {'formset':formset}
        
    return render(request,'Accounts/order_form.html',context)

def updateOrder(request,pk):
      order = Order.objects.get(id=pk)
      form = OrderForm(instance=order)

      if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        # print('Printing POST',request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
      context = {'form':form}

      return render(request,'Accounts/order_form.html',context)

def deleteOrder(request,pk):

    order = Order.objects.get(id=pk)

    if request.method == 'POST':
            order.delete()
            return redirect('/')

    context = {'item':order}
    return render(request,'Accounts/delete.html',context)





