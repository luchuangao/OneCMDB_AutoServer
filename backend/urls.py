from django.conf.urls import url,include
from django.contrib import admin
from backend import views
urlpatterns = [
    url(r'^curd.html$', views.curd),
    url(r'^curd_json.html$', views.curd_json),
]





