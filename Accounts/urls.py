from django.urls import path
from . import views


urlpatterns =[
    path("", views.index, name="index"),
    path("sign_in/", views.sign_in, name="sign_in"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("profile/", views.sign_up, name="profile"),
    path("logout/", views.sign_up, name="logout"),
]