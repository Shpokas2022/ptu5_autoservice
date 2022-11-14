from django.contrib import admin
from . import models


class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('service', 'quantity', 'price', 'total', 'order')
    ordering = ('order', 'id')
    list_filter = ('order', )


class OrderLineInline(admin.TabularInline):
    model = models.OrderLine
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineInline,)
    list_filter = ('date', 'status')


admin.site.register(models.Car)
admin.site.register(models.CarModel)
admin.site.register(models.Service)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderLine, OrderLineAdmin)
