from django.apps import AppConfig

class MarketplaceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'marketplace'
    verbose_name = "المتجر"  # اسم التطبيق يظهر في لوحة التحكم بالعربي
