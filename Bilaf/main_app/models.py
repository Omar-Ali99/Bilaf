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
    
class Cart(models.Model):
    STATUS_CHOICES = (
        
        ('Pending', 'Pending'),
        ('Submited', 'Submited'),
        ('Active', 'Active'),
        ('Declined', 'Declined'),
        ('Done', 'Done'),
    )
    DELIVERY_CHOICES = (
        ('Pick_Up', 'Pick Up'),
        ('Delivery', 'Delivery')
    )
    PAYMENT_CHOICES = (
        ('cod','Cash on Delivery')
        
    )

    store = models.ForeignKey(Store, on_delete=models.CASCADE)  
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices= STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    delivery_option = models.CharField(max_length=50,choices= DELIVERY_CHOICES)
    payment_option = models.CharField(max_length=50, choices= PAYMENT_CHOICES)
    

def __str__(self) -> str:
        return f"{self.store} - {self.customer}"

class CartItem(models.Model):
     cart = models.ForeignKey(User, on_delete=models.CASCADE)
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
     quantity = models.PositiveIntegerField()
     