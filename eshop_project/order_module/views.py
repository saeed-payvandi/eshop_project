from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from product_module.models import Product

# Create your views here.


def add_product_to_order(request: HttpRequest):
    product_id = request.GET.get('product_id')
    count = request.GET.get('count')

    if request.user.is_authenticated:
        product = Product.objects.filter(pk=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            pass
    else:
        return JsonResponse({
            'status': 'not_auth'
        })
    