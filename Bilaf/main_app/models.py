from django.db import models
from django.contrib.auth.models import User
from users_app.models import Store

# Create your models here.
class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.FloatField()
    name = models.CharField(max_length=2048)
    description = models.TextField()
    image = models.ImageField(upload_to="images/",default="images/placeholder.png")

    def __str__(self) -> str:
        return f"{self.name}"
