from django.urls import path
from . import views


urlpatterns = [
        path('', views.index, name='index'),
        path('oi', views.oi, name='oi'),
        path('counter', views.counter, name='counter'),
        ]
