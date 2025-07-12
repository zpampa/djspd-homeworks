from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.cars_list_view, name='car_list'),
    path('cars/<int:car_id>/', views.car_details_view, name='car_detail'),
    path('cars/<int:car_id>/sales/', views.sales_by_car, name='car_sales'),
]