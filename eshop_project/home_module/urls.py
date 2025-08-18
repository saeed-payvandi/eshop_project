from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    # path('', TemplateView.as_view(template_name = 'home_module/index_page.html'))
    path('', views.HomeView.as_view(), name='home_page'),
    path('about-us', views.AboutView.as_view(), name='about_page')
    # path('', views.index_page, name='home_page'),
    # path('site-header', views.site_header_component, name='site_header_component'),
    # path('site-footer', views.site_footer_component, name='site_footer_component'),
]