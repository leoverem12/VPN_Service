from django.contrib import admin
from .models import Location, Subscription, Service

# Register your models here.


admin.site.register([Location, Subscription, Service])