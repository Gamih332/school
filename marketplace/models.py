from django.db import models
from users.models import CustomUser

class Category(models.Model):
    name = models.CharField("اسم الفئة", max_length=100)

    class Meta:
        verbose_name = "فئة"
        verbose_name_plural = "الفئات"

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField("عنوان المنتج", max_length=200)
    description = models.TextField("وصف المنتج")
    file = models.FileField("ملف المنتج", upload_to='products/')
    price = models.DecimalField("السعر", max_digits=8, decimal_places=2)
    author = models.ForeignKey(CustomUser, verbose_name="المؤلف", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="الفئة", on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField("تاريخ الإضافة", auto_now_add=True)

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.title
