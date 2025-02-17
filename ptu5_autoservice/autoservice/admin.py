from django.contrib import admin
from . import models


class OrderLineAdmin(admin.ModelAdmin):
    # list_display = ('service', 'quantity', 'price', 'total', 'order')
    list_display = ('service', 'quantity', 'price', 'order')
    ordering = ('order', 'id')
    list_filter = ('order', )


class OrderLineInline(admin.TabularInline):
    model = models.OrderLine
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineInline,)
    list_filter = ('date', 'status')
    list_display = ('id', 'date', 'total', 'car', 'owner')
    list_editable = ('owner',)

class CarAdmin(admin.ModelAdmin):
    list_display = ('client', 'car_model', 'plate', 'vin')
    list_filter = ('client', 'car_model')
    search_fields = ('vin', 'plate')
    


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


admin.site.register(models.Car, CarAdmin)
admin.site.register(models.CarModel)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderLine, OrderLineAdmin)
