from django.shortcuts import render
from .models import Product

def home(request):
    product = Product.objects
    return render(request, 'prod/product.html',{'product':product})
