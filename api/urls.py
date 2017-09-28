from django.conf.urls import url,include
from django.contrib import admin
from api import views

urlpatterns = [
    url(r'^asset.html$', views.asset),
]
