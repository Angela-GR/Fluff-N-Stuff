from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

#This page is to link our admin page info to our html pages.

#Opening Page
def home(request):
    return render(request,"accounts/index.html")

#Dashboard Page(where we can see customer's info)

#Products Page
def products(request):
    return render(request, "accounts/products.html", {"products":products})

#Customers Page
def customers(request):
    return render(request, "accounts/customers.html")