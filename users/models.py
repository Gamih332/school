from django.db import models
from django.contrib.auth.models import AbstractUser

# توسيع نموذج المستخدم الافتراضي إذا أحببت لاحقًا
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    role_choices = [
        ('teacher', 'معلم/معلمة'),
        ('student', 'طالب/طالبة'),
    ]
    role = models.CharField(max_length=20, choices=role_choices, default='teacher')

    def __str__(self):
        return self.username
