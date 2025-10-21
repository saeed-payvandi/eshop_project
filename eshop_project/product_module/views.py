from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpRequest
from django.db.models import Avg, Min, Max, Count
from django.views.generic.base import TemplateView, View
from django.views.generic import ListView, DetailView
from .models import Product, ProductCategory, ProductBrand, ProductVisit, ProductGallery, ProductTag
from site_module.models import SiteBanner
from utils.http_service import get_client_ip
from utils.convertors import group_list


# Create your views here.


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 6

    def get_context_data(self, **kwargs):
        # print('context_data')
        context = super(ProductListView, self).get_context_data(**kwargs)
        query = Product.objects.all()
        product: Product = query.order_by('-price').first()
        db_max_price = product.price if product is not None else 0
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('end_price') or db_max_price
        context['banners'] = SiteBanner.objects.filter(is_active=True, position__iexact=SiteBanner.SiteBannerPositions.product_list)

        return context

    def get_queryset(self):
        # print('query_set')
        query = super(ProductListView, self).get_queryset()
        # print(self.kwargs)
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')
        request: HttpRequest = self.request
        # print(request.GET)
        start_price = request.GET.get('start_price')
        end_price = request.GET.get('end_price')

        if start_price is not None:
            query = query.filter(price__gte=start_price)

        if end_price is not None:
            query = query.filter(price__lte=end_price)

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
        context['banners'] = SiteBanner.objects.filter(is_active=True, position=SiteBanner.SiteBannerPositions.product_detail)
        galleries = list(ProductGallery.objects.filter(product_id=loaded_product.id).all())
        galleries.insert(0, loaded_product)
        context['product_galleries_group'] = group_list(galleries, 3)
        context['related_product'] = group_list(list(Product.objects.filter(brand_id=loaded_product.brand_id).exclude(pk=loaded_product.id).all()[:12]), 3)
        # request: HttpRequest = self.request
        # print(request.META.get('HTTP_X_FORWARDED_FOR'))
        # print(request.META.get('REMOTE_ADDR'))
        user_ip = get_client_ip(self.request)
        user_id = None
        if self.request.user.is_authenticated:
            user_id = self.request.user.id
        has_been_visited = ProductVisit.objects.filter(ip__iexact=user_ip, product_id=loaded_product.id).exists()
        if not has_been_visited:
            new_visit = ProductVisit(ip=user_ip, user_id=user_id, product_id=loaded_product.id)
            new_visit.save()
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


# def product_database_relationship(request):
#     category: ProductCategory = ProductCategory.objects.all()[0]
#     print('category: ', category)
#     brand: ProductBrand = ProductBrand.objects.all()[2]
#     print('brand: ', brand)
#     product: Product = Product.objects.all()[0]
#     print('product: ', product)
#     tag: ProductTag = ProductTag.objects.all()[0]
#     print('tag: ', tag)
#     visit: ProductVisit = ProductVisit.objects.all()[0]
#     print('visit: ', visit)
#     print('category.product_categories: ', category.product_categories.all())  # set relatedname:'product_categories'
#     print('brand.product_set: ', brand.product_set.all())
#     print('product.category: ', product.category.all())  # use .all() because relationship is manyTomany
#     print('product.brand: ', product.brand)
#     print('product.product_tags: ', product.product_tags.all())   # set realatedname: 'product_tags'
#     print('product.productvisit_set: ', product.productvisit_set.all())
#     print('tag.product: ', tag.product)
#     print('visit.product: ', visit.product)
#
#     return redirect('home_page')


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
