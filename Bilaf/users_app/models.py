from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13)
    # address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username}"


class Store(models.Model):
    CHOICES = (
        ("Saudi-Arabian", "Saudi-Arabian"),
        ("Syrian", "Syrian"),
        ("Egyptian", "Egyptian"),
        ("Indian", "Indian"),
        ("Chinese", "Chinese"),
        ("Italian", "Italian"),
        ("Mixed", "Mixed"),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=40)
    category = models.CharField(max_length=100, choices=CHOICES)
    logo = models.ImageField(upload_to="images/", default="images/default_logo.jpeg")
    about = models.TextField()
    pick_up_enabled = models.BooleanField(default=True)
    delivery_enabled = models.BooleanField(default=True)
    twitter_link = models.URLField(blank=True, default="")
    instagram_link = models.URLField(blank=True, default="")
    snapchat_link = models.URLField(blank=True, default="")

    def __str__(self) -> str:
        return f"{self.store_name} By {self.owner}"


class Address(models.Model):
    CHOICES = (("Riyadh", "Riyadh"),)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, choices=CHOICES)
    # distrect = models.CharField ()
    # location = models.PointField(null=True, blank=True)
