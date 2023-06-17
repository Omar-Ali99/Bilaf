from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    # address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return super() + f"{self.user.username}"

class Store(models.Model):
    CHOICES = (
    ('Saudi-Arabian', 'Saudi-Arabian'),
    ('Syrian', 'Syrian'),
    ('Egyptian', 'Egyptian'),
    ('Indian', 'Indian'),
    ('Chinese', 'Chinese'),
    ('Italian', 'Italian'),
    ('Mixed', 'Mixed'),
    
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField (max_length= 40)
    category = models.CharField(max_length=100, choices=CHOICES)
    logo = models.ImageField(upload_to="images/", default="images/default_logo.jpeg")
    about = models.TextField()
    commercial_registration = models.IntegerField()
    pick_up_enabled = models.BooleanField (default=True)
    delivery_enabled = models.BooleanField (default=True)
    twitter_link = models.URLField()
    instagram_link = models.URLField()
    snapchat_link = models.URLField()

    def __str__(self) -> str:
        return f"{self.store_name}"

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.FloatField()
    name = models.CharField(max_length=2048)
    description = models.TextField()
    image = models.ImageField(upload_to="images/",default="images/placeholder.png")

    def __str__(self) -> str:
        return f"{self.name}"



# class Address(models.Model):
#     CHOICES = (
#         ('Riyadh', 'Riyadh'),
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     city = models.CharField()
#     distrect = models.CharField ()
#     # map_pointer = models.po

