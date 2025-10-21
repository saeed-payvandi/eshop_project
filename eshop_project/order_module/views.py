from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from product_module.models import Product
from .models import Order, OrderDetail

# Create your views here.


def add_product_to_order(request: HttpRequest):
    product_id = request.GET.get('product_id')
    count = request.GET.get('count')

    if request.user.is_authenticated:
        product = Product.objects.filter(pk=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            # current_order = Order.objects.filter(is_paid=False, user_id=request.user.id).first()
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id) # use created variable because get_or_create() method return tuple
            current_order_detail: OrderDetail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += int(count)
                current_order_detail.save()
            else:
                new_detail: OrderDetail = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
                new_detail.save()

            return JsonResponse({
                'status': 'success'
            })
        else:
            return JsonResponse({
                'status': 'not_found'
            })
    else:
        return JsonResponse({
            'status': 'not_auth'
        })
