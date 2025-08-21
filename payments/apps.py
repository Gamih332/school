from django.apps import AppConfig

class PaymentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payments'
    verbose_name = "المدفوعات"  # اسم التطبيق يظهر في لوحة التحكم بالعربي
