from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from site_module.models import SiteSetting, FooterLinkBox, Slider
from product_module.models import Product
from utils.convertors import group_list

# Create your views here.


# class HomeView(View):
#     def get(self, request):
#         context = {
#             'data': 'this is data',
#         }
#         return render(request, 'home_module/index_page.html', context)


class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slider = Slider.objects.filter(is_active=True)
        context['sliders'] = slider
        latest_products = Product.objects.filter(is_active=True, is_delete=False).order_by('-id')[:12]
        # print(latest_products)
        # print(group_list(latest_products, 1))
        context['latest_products'] = group_list(latest_products, 1)

        return context


# def index_page(request):
#     return render(request, 'home_module/index_page.html')


def site_header_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting,
    }
    return render(request, 'shared/site_header_component.html', context)


def site_footer_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    footer_link_boxes = FooterLinkBox.objects.all()
    context = {
        'site_setting': setting,
        'footer_link_boxes': footer_link_boxes,
    }
    return render(request, 'shared/site_footer_component.html', context)


class AboutView(TemplateView):
    template_name = 'home_module/about_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        site_setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = site_setting
        return context
