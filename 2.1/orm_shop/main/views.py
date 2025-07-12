from django.http import Http404
from django.shortcuts import render, get_object_or_404

from main.models import Car, Sale


def cars_list_view(request):
    cars = Car.objects.all()
    return render(request, 'main/list.html', {'cars': cars})


def car_details_view(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'main/details.html', {'car': car})


def sales_by_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    sales = Sale.objects.filter(car=car)
    return render(request, 'main/sales.html', {'car': car, 'sales': sales})
