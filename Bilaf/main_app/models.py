from django.db import models
from django.contrib.auth.models import User
from users_app.models import Store

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=128)
    logo = models.ImageField(upload_to="images/",default="images/placeholder.png")
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"




class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=2048)
    description = models.TextField()
    image = models.ImageField(upload_to="images/",default="images/placeholder.png")

    def __str__(self) -> str:
        return f"{self.name}"
    

