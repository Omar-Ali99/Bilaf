from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class merchant_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    merchant_name = models.CharField(max_length=120)

def __str__(self) -> str:
        return f"{self.merchant_name}"

class customer_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
