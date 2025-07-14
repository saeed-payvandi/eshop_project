from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # # readonly_fields = ['slug', ]
    # prepopulated_fields = {
    #     'slug': ['title']
    # }
    # list_display = ['__str__', 'price', 'rating', 'is_active', 'category', 'product_information']
    # list_filter = ['rating', 'is_active']
    # list_editable = ['rating', 'is_active']
    list_filter = ['category', 'is_active']
    list_display = ['title', 'price', 'is_active', 'is_delete']
    list_editable = ['price', 'is_active']


@admin.register(models.ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


# @admin.register(models.ProductInformation)
# class ProductInformationAdmin(admin.ModelAdmin):
#     pass


@admin.register(models.ProductTag)
class ProductTagAdmin(admin.ModelAdmin):
    pass


@admin.register(models.ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    pass


# admin.site.register(models.Product, ProductAdmin)
# admin.site.register(models.ProductCategory, ProductCategoryAdmin)
# admin.site.register(models.ProductInformation)
# admin.site.register(models.ProductTag)
# admin.site.register(models.ProductBrand, ProductBrandAdmin)
