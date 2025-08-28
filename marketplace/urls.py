# marketplace/urls.py

from django.urls import path
from . import views

app_name = "marketplace"  # لتسهيل استخدام أسماء الروابط في القوالب {% url 'marketplace:home' %}

urlpatterns = [
    # الصفحة الرئيسية للمتجر
    path('', views.home, name='home'),

    # أمثلة لمسارات إضافية (مستقبلية)
    path('products/', views.product_list, name='product_list'),        # قائمة المنتجات
    path('products/<int:pk>/', views.product_detail, name='product_detail'),  # تفاصيل المنتج
    path('cart/', views.cart_view, name='cart'),                       # سلة المشتريات
    path('checkout/', views.checkout, name='checkout'),                # صفحة الدفع
]
