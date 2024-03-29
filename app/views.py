from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *


#Start of Sign up System
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

#This page is to link our admin page info to our html pages.

#Opening Page
def home(request):
    return render(request,"accounts/index.html")

#Dashboard Page(where we can see customer's info)

#Products Page
def products(request):
    products = Product.objects.all()
    return render(request, "accounts/products.html", {"products":products})

#Customers Page
def customers(request):
    customers = Customer.objects.all()
    return render(request, "accounts/customers.html", {"customers":customers})

def dashboard(request):
    return render(request,"accounts/dashboard.html")


#Add Student Page
def add(request):
    form = CustomerForm(request.POST or None)
    # customer = Student.objects.all()
    if form.is_valid():
        form.save()
    return render(request,"add.html", {"form":form})


#Sign up
def sign_up(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    context = {"form":form}
    return render (request, "accounts/signup.html", context)


def login_in(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('home')
    context = {"form":form}
    return render (request, "accounts/login.html", context)

# delete/update
def delete_customer(request, id):
    if request.method == "POST":
        delete = Product.objects.get(id = id)
        delete.delete()
        return redirect(home)
    else:
        return render(request, "products.html")

def update_customer(request):
    if request.method == "POST":
        item = request.POST.get("product")
        price = request.POST.get("price")
        change = Product.objects.get(item = item)
        change.price = price
        change.save()
        return redirect('home')
    else:
        return render(request, "update.html")