from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'amount', 'status', 'payment_date')
    list_filter = ('status', 'payment_date')
    search_fields = ('user__username', 'product__title')
