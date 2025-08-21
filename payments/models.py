from django.db import models
from users.models import CustomUser
from marketplace.models import Product

class Payment(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="المستخدم", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="المنتج", on_delete=models.CASCADE)
    amount = models.DecimalField("المبلغ", max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField("تاريخ الدفع", auto_now_add=True)
    STATUS_CHOICES = [
        ('pending', 'قيد الانتظار'),
        ('completed', 'مكتمل'),
        ('failed', 'فشل'),
    ]
    status = models.CharField("حالة الدفع", max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        verbose_name = "دفع"
        verbose_name_plural = "المدفوعات"

    def __str__(self):
        return f"{self.user.username} - {self.product.title} - {self.status}"
