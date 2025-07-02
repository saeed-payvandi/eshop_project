from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import Http404


# Create your views here.

def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }

    return render(request, 'product_module/product_list.html', context)


def product_detail(request, product_id):
    # try:
    #     product = Product.objects.get(id=product_id)
    # except:
    #     raise Http404()
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'product_module/product_detail.html', context)
