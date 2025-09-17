# school/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# استدعاء الصفحات من تطبيق marketplace
from marketplace.views import (
    home,
    portfolio_view,
    product_list,
    product_detail,
    cart_view,
    checkout,
    certificates_view
)

urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية عند زيارة الرابط '/'
    path('', home, name='home'),

    # صفحة البورتفوليو
    path('portfolio/', portfolio_view, name='portfolio'),

    # صفحة قائمة المنتجات
    path('products/', product_list, name='product_list'),

    # صفحة تفاصيل منتج برقم محدد (مثال: /products/1/)
    path('products/<int:pk>/', product_detail, name='product_detail'),

    # سلة المشتريات
    path('cart/', cart_view, name='cart'),

    # صفحة الدفع
    path('checkout/', checkout, name='checkout'),

    # صفحة الشهادات
    path('certificates/', certificates_view, name='certificates'),

    # روابط التطبيقات الخاصة
    path('users/', include('users.urls')),              # روابط إدارة المستخدمين
    path('marketplace/', include('marketplace.urls')),  # روابط المتجر
    path('payments/', include('payments.urls')),        # روابط الدفع
]

# أثناء التطوير: خدمة ملفات static و media
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
