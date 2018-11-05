from django.shortcuts import render
from .models import Specs

def spec(request):
    Specifications = Specs.objects
    return render(request,'specs/specification.html',{'spec':Specifications})
