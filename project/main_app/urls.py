from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="Home"),
    path("about/", views.about, name="about"),
]
