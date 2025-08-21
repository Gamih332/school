from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField("رقم الهاتف", max_length=20, blank=True, null=True)
    ROLE_CHOICES = [
        ('teacher', 'معلم/معلمة'),
        ('student', 'طالب/طالبة'),
    ]
    role = models.CharField("الدور", max_length=20, choices=ROLE_CHOICES, default='teacher')

    class Meta:
        verbose_name = "مستخدم"
        verbose_name_plural = "المستخدمون"

    def __str__(self):
        return self.username
