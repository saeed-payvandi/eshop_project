from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from product_module.models import Product
from .models import Order, OrderDetail
from datetime import datetime
import requests
import json
import os

# Create your views here.

MERCHANT = os.getenv('MERCHANT')
ZP_API_REQUEST = 'https://sandbox.zarinpal.com/pg/v4/payment/request.json'
ZP_API_VERIFY = 'https://sandbox.zarinpal.com/pg/v4/payment/verify.json'
ZP_API_STARTPAY = 'https://sandbox.zarinpal.com/pg/StartPay/{authority}'
# amount = 11000 # Rials / Required
description = 'تهایی کردن خرید شما از سایت ما' # Required
email = '' # Optional
mobile = '' # Optional
# Important: need to edit for really server
CallbackURL = 'http://127.0.0.1:8000/order/verify-payment/'



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


@login_required
def request_payment(request: HttpRequest):
    current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
    total_price = current_order.calculate_total_price()
    if total_price == 0:
        return redirect(reverse('user_basket_page'))
    req_data = {
        "merchant_id": MERCHANT,
        "amount": total_price * 10,
        "callback_url": CallbackURL,
        "description": description,
        # "metadata": {"email": email, "mobile": mobile}
    }
    req_header = {"accept": "application/json", "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(req_data), headers=req_header)
    authority = req.json()['data']['authority']
    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error Code: {e_code}, Error Message: {e_message}")        


@login_required
def verify_payment(request: HttpRequest):
    current_order, created = Order.objects.get_or_create(is_paid=False, user_id=request.user.id)
    total_price = current_order.calculate_total_price()
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json", "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": total_price * 10,
            "authority": t_authority,
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
                for detail in current_order.orderdetail_set.all():
                    detail.final_price = detail.product.price
                    detail.save()
                current_order.is_paid = True
                current_order.payment_date = datetime.now()
                current_order.save()
                # return HttpResponse('Transation succes.\nRefID: ' + str(req.json()['data']['ref_id']))
                ref_str = str(req.json()['data']['ref_id'])
                context = {
                    'success': f'تراکنش شما با کد پیگیری {ref_str} با موفقیت انچام شد'
                }
                return render(request, 'order_module/payment_result.html', context)
            elif t_status == 101:
                # return HttpResponse('Transaction submitted : ' + str(req.json()['data']['message']))
                context = {
                    'info': 'این تراکنش قبلا ثبت شده است'
                }
                return render(request, 'order_module/payment_result.html', context)
            else:
                # return HttpResponse('Transaction failed.\nStatus : ' + str(req.json()['data']['message']))
                context = {
                    'error': str(req.json()['data']['message'])
                }
                return render(request, 'order_module/payment_result.html', context)
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            # return HttpResponse(f"Error Code: {e_code}, Error Message: {e_message}")
            context = {
                    'error': f"Error Code: {e_code}, Error Message: {e_message}"
                }
            return render(request, 'order_module/payment_result.html', context)

    else:
        # return HttpResponse('Transaction failed or canceled by user')
        context = {
                    'error': 'پرداخت با خطا مواجه شد / کاربر از پرداخت منصرف شد'
                }
        return render(request, 'order_module/payment_result.html', context)