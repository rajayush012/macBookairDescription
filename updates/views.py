from django.shortcuts import render
from .models import Updates

def update(request):
    Upd = Updates.objects
    return render(request,'update/updates.html',{'updates':Upd})
