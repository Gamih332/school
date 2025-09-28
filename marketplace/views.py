from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """
    الصفحة الرئيسية للمتجر
    تعرض المنتجات أو المحتوى الأساسي
    """
    context = {
        "page_title": "الرئيسية - متجر المعلمين",
        "page_type": "home",
        "welcome_message": "مرحبًا بكم في متجر المعلمين - ملفات إنجاز، شهادات، أفكار تعليمية، وأوراق عمل جاهزة للطباعة.",
    }
    return render(request, "home.html", context)


def portfolio_view(request):
    """
    صفحة العرض التجريبي للمحفظة أو المشاريع
    """
    context = {
        "page_title": "البورتفوليو - متجر المعلمين",
        "page_type": "portfolio",
        "welcome_message": "استعرض مجموعة من الأعمال والملفات التعليمية المميزة.",
    }
    return render(request, "home.html", context)


def product_list(request):
    """
    قائمة المنتجات
    """
    context = {
        "page_title": "المنتجات - متجر المعلمين",
        "page_type": "products",
        "welcome_message": "تصفح جميع منتجاتنا التعليمية المميزة.",
    }
    return render(request, "home.html", context)


def product_detail(request, pk):
    """
    تفاصيل المنتج
    """
    context = {
        "page_title": f"تفاصيل المنتج {pk} - متجر المعلمين",
        "page_type": "product_detail",
        "welcome_message": f"تفاصيل المنتج رقم {pk} (قريباً).",
    }
    return render(request, "home.html", context)


def cart_view(request):
    """
    سلة المشتريات
    """
    context = {
        "page_title": "سلة المشتريات - متجر المعلمين",
        "page_type": "cart",
        "welcome_message": "هذه سلة المشتريات الخاصة بك.",
    }
    return render(request, "home.html", context)


def checkout(request):
    """
    صفحة الدفع
    """
    context = {
        "page_title": "الدفع - متجر المعلمين",
        "page_type": "checkout",
        "welcome_message": "أكمل عملية الدفع بأمان وسهولة.",
    }
    return render(request, "home.html", context)


def certificates_view(request):
    """
    صفحة الشهادات
    """
    context = {
        "page_title": "الشهادات - متجر المعلمين",
        "page_type": "certificates",
        "welcome_message": "مجموعة شهادات تقدير جاهزة للتعديل والطباعة.",
    }
    return render(request, "home.html", context)
