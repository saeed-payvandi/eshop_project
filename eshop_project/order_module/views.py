from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from product_module.models import Product
from .models import Order, OrderDetail

# Create your views here.


def add_product_to_order(request: HttpRequest):
    product_id = int(request.GET.get('product_id'))
    count = int(request.GET.get('count'))
    if count < 1:
        # count = 1
        return JsonResponse({
            'status': 'invalid_count',
            'text': 'مقدار وارد شده معتبر نمی باشد',
            'icon': 'warning',
            'confirm_button_text': 'مرسی از شما',
        })

    if request.user.is_authenticated:
        product = Product.objects.filter(pk=product_id, is_active=True, is_delete=False).first()
        if product is not None:
            # current_order = Order.objects.filter(is_paid=False, user_id=request.user.id).first()
            current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id) # use created variable because get_or_create() method return tuple
            current_order_detail: OrderDetail = current_order.orderdetail_set.filter(product_id=product_id).first()
            if current_order_detail is not None:
                current_order_detail.count += count
                current_order_detail.save()
            else:
                new_detail: OrderDetail = OrderDetail(order_id=current_order.id, product_id=product_id, count=count)
                new_detail.save()

            return JsonResponse({
                'status': 'success',
                'text': 'محصول مورد نظر با موفقیت به سبد خرید شما اضافه شد',
                'icon': 'success',
                'confirm_button_text': 'باشه ممنونم',
            })
        else:
            return JsonResponse({
                'status': 'not_found',
                'text': 'محصول مورد نظر یافت نشد ',
                'icon': 'error',
                'confirm_button_text': 'مرسییی',
            })
    else:
        return JsonResponse({
            'status': 'not_auth',
            'text': 'برای افزودن محصول به سبد خرید ابتدا می بایست وارد سایت شوید',
            'icon': 'error',
            'confirm_button_text': 'ورود به سایت',
        })
