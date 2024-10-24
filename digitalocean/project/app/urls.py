from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout'),
    path('signup', views.signup, name='signup'),
    path('products', views.products, name='products'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('register', views.register, name='register'),
]
