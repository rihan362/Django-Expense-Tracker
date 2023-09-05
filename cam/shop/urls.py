
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.foam,name='foam'),
    path('sign',views.handlesignup,name='handlesignup'),
    path('wings',views.main,name='wings'),
    path('login',views.handlelogin,name='handlelogin'),
    path('logout',views.handlelogout,name='handlelogout'),
    path('show',views.represent,name='show'),
    path('bar',views.bar,name='bar'),
]
