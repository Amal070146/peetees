from django.shortcuts import render
from .models import Grocery,Bakery,Stationary,Electrical,Dairy,Fruit,Vegetable


# Create your views here.

def home(request):
    return render( request,'home.html')

def grocery(request):
    grocery_list = {'grocery':Grocery.objects.all()}
    return render( request,'grocery.html', grocery_list)

def bakery(request):
    grocery_list = {'bakery':Bakery.objects.all()}
    return render( request,'bakery.html', grocery_list)

def electrical(request):
    electrical_list = {'electrical':Electrical.objects.all()}
    return render( request,'electrical.html', electrical_list)

def stationary(request):
    stationary_list = {'stationary':Stationary.objects.all()}
    return render( request,'stationary.html', stationary_list)

def dairy(request):
    dairy_list = {'dairy':Dairy.objects.all()}
    return render( request,'dairy.html', dairy_list)

def fruits(request):
    fruits_list = {'fruits':Fruit.objects.all()}
    return render( request,'fruits.html', fruits_list)

def vegetables(request):
    vegetables_list = {'vegetables':Vegetable.objects.all()}
    return render( request,'vegetables.html', vegetables_list)
