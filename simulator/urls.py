from django.urls import path
from . import views

urlpatterns = [
    path('', views.simulate_sales, name='simulate_sales'),
]
