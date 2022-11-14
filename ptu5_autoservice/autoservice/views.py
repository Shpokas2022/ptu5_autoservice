from django.shortcuts import render
from . import models


def index(request):
    return render(request, 'autoservice/index.html', {
        'cars_count': models.Car.objects.count(),
        'services_count': models.Service.objects.count(),
        'orders_count': models.Order.objects.count(),
    })

