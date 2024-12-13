from django.shortcuts import render
from .models import Brand, Car

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'cars/brand_list.html', {'brands': brands})

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})
