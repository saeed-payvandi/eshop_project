from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory
from django.http import Http404
from django.db.models import Avg, Min, Max


# Create your views here.

def product_list(request):
    # console = ProductCategory(title='پلی استیشن', url_title='playstation')
    # console.save()
    # ps4 = Product(title='play station 4', price=17000000, category= console, short_description='ps_4', rating=4)
    # ps4.save()
    products = Product.objects.all().order_by('-title')
    number_of_products = products.count()
    # avg_rating = products.aggregate(Avg("rating"), Avg("price"), Min("price"), Max("price"))
    context = {
        'products': products,
        'total_number_of_products': number_of_products,
        # 'average_ratings': avg_rating,
    }

    return render(request, 'product_module/product_list.html', context)


def product_detail(request, slug):
    # try:
    #     product = Product.objects.get(id=product_id)
    # except:
    #     raise Http404()
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'product_module/product_detail.html', context)
