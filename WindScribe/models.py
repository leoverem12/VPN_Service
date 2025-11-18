from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    location = models.CharField(max_length=256)


class Subscription(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    locations = models.ManyToManyField(Location)

class Service(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ipv_4_ext = models.GenericIPAddressField(unique=True, null=True, blank=True, default=None)
    price_per_month_ext = models.FloatField(default=0)
    ipv_4_local = models.GenericIPAddressField(unique=True)
    price_per_month_4_local = models.FloatField(default=0)
    ipv_6 = models.GenericIPAddressField(unique=True)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)