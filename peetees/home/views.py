from django.shortcuts import render
from .models import Grocery


# Create your views here.

def home(request):
    return render( request,'home.html')

def grocery(request):
    grocery_list = Grocery.objects.all()
    return render( request,'grocery.html', grocery_list)

