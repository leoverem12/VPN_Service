from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpo
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.contrib import messages
from django.core.cache import cache

from .forms import ProfileForm, UserForm

# Create your views here.


def sign_up(request: HttpRequest):
    form = SignUpo(data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request=request, message="KO")
        return redirect("sign_in")
    return render(request, "sign_up.html", dict(form=form))


def sign_in(request: HttpRequest):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method =="POST" and form.is_valid():
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"]
        )
        if not user:
            messages.warning(request, "NO!")
            return redirect("sign_in")
        
        login(request=request, user=user)
        return redirect("index")
    return render(request, "sign_in.html", dict(form=form))


@login_required
def index(request: HttpRequest):
    return render(request, "index.html")

@login_required
def logout_user(request: HttpRequest):
    logout(request)
    return redirect("sign_in")

@login_required
def profile(request: HttpRequest):
    user_form = UserForm(data=request.POST or None, instace=request.user)
    profile_form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user.details)
    if request.method == "POST" and user_form.changed_data or request.method == "POST" and profile_form.changed_data:
        user_form.save()
        profile_form.save()
        messages.info(request, "Succ")
        return redirect("profile")
    return render(request, "profile.html", context=dict(user_form=user_form, profile_form=profile_form))