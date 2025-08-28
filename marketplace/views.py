# marketplace/views.py

from django.shortcuts import render

def home(request):
    """
    الصفحة الرئيسية للمتجر
    تعرض المنتجات أو المحتوى الأساسي
    """
    context = {
        "page_title": "الرئيسية - متجر المعلمين",
        "welcome_message": "مرحبًا بكم في متجر المعلمين - ملفات إنجاز، شهادات، أفكار تعليمية، وأوراق عمل جاهزة للطباعة.",
    }
    return render(request, "home.html", context)
