from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(models.OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    pass


# admin.site.register(models.Order, OrderAdmin)
# admin.site.register(models.OrderDetail. OrderDetailAdmin)
