from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpRequest
from django.db.models import Avg, Min, Max, Count
from django.views.generic.base import TemplateView, View
from django.views.generic import ListView, DetailView
from .models import Product, ProductCategory, ProductBrand


# Create your views here.


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 6

    def get_queryset(self):
        query = super(ProductListView, self).get_queryset()
        # print(self.kwargs)
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')

        if category_name is not None:
            query = query.filter(category__url_title__iexact=category_name)

        if brand_name is not None:
            query = query.filter(brand__url_title__iexact=brand_name)

        return query


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_product = self.object
        request = self.request
        favorite_product_id = request.session.get('product_favorites')
        context['is_favorite'] = favorite_product_id == str(loaded_product.id)
        return context





class AddProductFavorite(View):
    def post(self, request):
        # print(dir(request))
        # print("GET:", request.GET)
        # print("POST:", request.POST)
        # print("BODY:", request.body)
        # print("FILES:", request.FILES)
        # print("COOKIES:", request.COOKIES)
        # print("META:", request.META)
        # print("USER:", request.user)
        product_id = request.POST['product_id']
        product = Product.objects.get(pk=product_id)
        request.session["product_favorites"] = product_id
        return redirect(product.get_absolute_url())


def product_categories_component(request: HttpRequest):
    product_categories = ProductCategory.objects.filter(is_active=True, is_delete=False)
    context = {
        'categories': product_categories,
    }
    return render(request, 'product_module/components/product_categories_component.html', context)


def product_brands_component(request: HttpRequest):
    product_brands = ProductBrand.objects.annotate(products_count=Count('product')).filter(is_active=True)
    context = {
        'brands': product_brands
    }
    return render(request, 'product_module/components/product_brands_component.html', context)


# class ProductListView(TemplateView):
#     template_name = 'product_module/product_list.html'

#     def get_context_data(self, **kwargs):
#         product = Product.objects.all().order_by('price')[:5]
#         context = super().get_context_data(**kwargs)
#         # context = super(ProductListView, self).get_context_data()
#         context['products'] = product
#         return context
    

# class ProductDetailView(TemplateView):
#     template_name = 'product_module/product_detail.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         slug = kwargs['slug']
#         product = get_object_or_404(Product, slug=slug)
#         context['product'] = product
#         return context


# def product_list(request):
#     # console = ProductCategory(title='پلی استیشن', url_title='playstation')
#     # console.save()
#     # ps4 = Product(title='play station 4', price=17000000, category= console, short_description='ps_4', rating=4)
#     # ps4.save()
#     # products = Product.objects.all().order_by('-title')
#     # number_of_products = products.count()
#     # avg_rating = products.aggregate(Avg("rating"), Avg("price"), Min("price"), Max("price"))
#     products = Product.objects.all().order_by('-price')[:5]
#     context = {
#         'products': products,
#         # 'total_number_of_products': number_of_products,
#         # 'average_ratings': avg_rating,
#     }
#
#     return render(request, 'product_module/product_list.html', context)


# def product_detail(request, slug):
#     # try:
#     #     product = Product.objects.get(id=product_id)
#     # except:
#     #     raise Http404()
#     product = get_object_or_404(Product, slug=slug)
#     context = {
#         'product': product,
#     }
#     return render(request, 'product_module/product_detail.html', context)
