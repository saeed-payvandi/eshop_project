from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product-list'),
    path('cat/<cat>', views.ProductListView.as_view(), name='product-categories-list'),
    path('brand/<brand>', views.ProductListView.as_view(), name='product-list-by-brands'),
    path('<slug:slug>', views.ProductDetailView.as_view(), name='product-detail'),
    path('product-favorite/', views.AddProductFavorite.as_view(), name='product-favorite'),
    # path('database-relationship/', views.product_database_relationship)
    # path('<int:pk>', views.ProductDetailView.as_view(), name='product-detail')
    # path('', views.product_list, name='product-list'),
    # path('<slug:slug>', views.product_detail, name='product-detail')
]
