from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # readonly_fields = ['slug', ]
    prepopulated_fields = {
        'slug': ['title']
    }
    list_display = ['__str__', 'price', 'rating', 'is_active']
    list_filter = ['rating', 'is_active']
    list_editable = ['rating', 'is_active']


# admin.site.register(models.Product, ProductAdmin)
