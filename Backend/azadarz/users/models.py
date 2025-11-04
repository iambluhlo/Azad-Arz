from django.db import models

class User(models.Model):
    STATUS_CHOICES = [
        ('active', 'فعال'),
        ('pending', 'در انتظار تأیید'),
        ('blocked', 'مسدود'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    joined = models.DateField(auto_now_add=True)
    balance = models.DecimalField(max_digits=15, decimal_places=0, default=0)

    def __str__(self):
        return self.name
# Create your models here.
