from django.urls import path

from . import views

urlpatterns =[
    path('index.html', views.interval_index),
    path('', views.get_home)
]