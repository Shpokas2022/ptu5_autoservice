from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import models
from . models import Car, Service, Order


def index(request):
    # return render(request, 'autoservice/index.html', {
    #     'cars_count': models.Car.objects.count(),
    #     'services_count': models.Service.objects.count(),
    #     'orders_count': models.Order.objects.count(),
    #     'visits_count': request.session.get('visits_count').count(),
    # })
    cars_count = Car.objects.count()
    services_count = Service.objects.count()
    orders_count = Order.objects.count()
    visits_count = request.session.get('visits_count', 1)
    request.session['visits_count'] = visits_count + 1
    
    context = {
        'cars_count': cars_count,
        'services_count': services_count,
        'orders_count': orders_count,
        'visits_count': visits_count,
    }

    return render(request, 'autoservice/index.html', context)

def car_list_view(request):
    car_list = models.Car.objects.all()
    search = request.GET.get('search')
    if search:
        car_list = car_list.filter(
            Q(client__icontains=search) |
            Q(plate__icontains=search) |
            Q(car_model__make__icontains=search) |
            Q(car_model__model__icontains=search)
        )
    paginator = Paginator(car_list, 4)
    page_number = request.GET.get('page')
    paged_cars = paginator.get_page(page_number)
    return render(request, 'autoservice/car_list.html', {
        'car_list': paged_cars,
    })

def car_detail_view(request, pk):
    return render(request, 'autoservice/car_detail.html', {
        'object': get_object_or_404(models.Car, pk=pk),
    })


class OrderListView(generic.ListView):
    model = models.Order
    paginate_by = 4
    template_name = 'autoservice/order_list.html'

    def get_queryset(self):
        queryset =  super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            try:
                queryset = queryset.filter(id__exact=search)
            except ValueError:
                queryset = queryset.filter(
                    Q(car__client__icontains=search) |
                    Q(car__plate__icontains=search)
                )
        return queryset


class OrderDetailView(generic.DetailView):
    model = models.Order
    template_name = 'autoservice/order_detail.html'
