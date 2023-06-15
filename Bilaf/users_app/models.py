from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    # address = models.OneToOneField(Address, on_delete=models.CASCADE)

class Store(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField (max_length= 40)
    logo = models.ImageField(upload_to="images/", default="default_logo.jpeg")
    about = models.TextField()
    commercial_registration = models.IntegerField()
    pick_up_enabled = models.BooleanField (default=True)
    delivery_enabled = models.BooleanField (default=True)
    twitter_link = models.URLField()
    instagram_link = models.URLField()
    snapchat_link = models.URLField()


# class Address(models.Model):
#     CHOICES = (
#         ('Riyadh', 'Riyadh'),
#     )
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     city = models.CharField()
#     distrect = models.CharField ()
#     # map_pointer = models.po

