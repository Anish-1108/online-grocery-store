"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('single_product/',views.single_product,name='single_product'),
    path('shop_details/<str:id>',views.shop_details,name='shop_details'),
    path('shoping_cart/',views.shoping_cart,name='shoping_cart'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('checkout/',views.checkout,name='checkout'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    path('forget_password/',views.forget_password,name='forget_password'),
    path('comefrom_password',views.comefrom_password,name='comefrom_password'),
    path('puls/<int:id>', views.puls, name='puls'),
    path('manus/<int:id>', views.manus, name='manus'),
    path('remov/<str:id>', views.remov, name='remov'),
    path('add_to_cart/<str:id>', views.add_to_cart, name='add_to_cart'),
    path('blog_details/',views.blog_details,name='blog_details'),
    path('address/',views.address,name='address'),
    path('searchview',views.searchview,name='searchview'),

]

      
     