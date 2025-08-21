from django.db import models
from users.models import CustomUser
from marketplace.models import Product

class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    status_choices = [
        ('pending', 'قيد الانتظار'),
        ('completed', 'مكتمل'),
        ('failed', 'فشل'),
    ]
    status = models.CharField(max_length=20, choices=status_choices, default='pending')

    def __str__(self):
        return f"{self.user.username} - {self.product.title} - {self.status}"
