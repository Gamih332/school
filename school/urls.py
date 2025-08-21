"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # روابط التطبيقات الخاصة
    path('users/', include('users.urls')),           # روابط إدارة المستخدمين
    path('marketplace/', include('marketplace.urls')),  # روابط المتجر
    path('payments/', include('payments.urls')),     # روابط الدفع
]

# إعداد ملفات الميديا أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
