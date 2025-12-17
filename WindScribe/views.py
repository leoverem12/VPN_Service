from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Subscription, Service
from .forms import SubForm
from django.http.request import HttpRequest
from faker import Faker

# Create your views here.

fake = Faker()

def get_subscriptions(request: HttpRequest):
    form = SubForm(data=request.POST or None)
    if request.method =='POST' and form.is_valid():
        subscription: Subscription = form.cleaned_data.get("sub")
        service, _ = Service.objects.get_or_create(user=request.user)

        service.ipv_4_local = fake.ipv4_private() if "ipv_4_local" in subscription.services else None
        service.ipv_4_ext = fake.ipv4_public() if "ipv_4_ext" in subscription.services else None
        service.ipv_6 = fake.ipv6() if "ipv_6" in subscription.services else None
        service.subscription = subscription

        service.save()
        return redirect("index")
    return render(request, "subscription.html", dict(form=form))