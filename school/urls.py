# school/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# استدعاء الصفحة الرئيسية من تطبيق المتجر
from marketplace.views import home  

urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية عند زيارة الرابط '/'
    path('', home, name='home'),

    # روابط التطبيقات الخاصة
    path('users/', include('users.urls')),              # روابط إدارة المستخدمين
    path('marketplace/', include('marketplace.urls')),  # روابط المتجر
    path('payments/', include('payments.urls')),        # روابط الدفع
]

# أثناء التطوير: خدمة ملفات static و media
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
