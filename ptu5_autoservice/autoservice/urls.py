from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.car_list_view, name='cars'),
    path('car/<int:pk>/', views.car_detail_view, name='car'),
]
