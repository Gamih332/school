from django.shortcuts import render
from django.http import HttpResponse

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


def portfolio_view(request):
    """
    صفحة العرض التجريبي للمحفظة أو المشاريع
    """
    return HttpResponse("صفحة Portfolio (تحت الإنشاء)")


def product_list(request):
    """
    قائمة المنتجات (placeholder مؤقت)
    """
    return HttpResponse("صفحة قائمة المنتجات (تحت الإنشاء)")


def product_detail(request, pk):
    """
    تفاصيل المنتج (placeholder مؤقت)
    """
    return HttpResponse(f"تفاصيل المنتج رقم {pk} (تحت الإنشاء)")


def cart_view(request):
    """
    سلة المشتريات (placeholder مؤقت)
    """
    return HttpResponse("سلة المشتريات (تحت الإنشاء)")


def checkout(request):
    """
    صفحة الدفع (placeholder مؤقت)
    """
    return HttpResponse("صفحة الدفع (تحت الإنشاء)")


def certificates_view(request):
    """
    صفحة الشهادات (placeholder مؤقت)
    """
    return HttpResponse("صفحة الشهادات (تحت الإنشاء)")
