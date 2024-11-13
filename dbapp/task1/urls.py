from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('card/', views.cart_page, name='card'),
    path('product/', views.shop_page, name='product'),
    path('register/django', views.sign_up_by_django, name='register'),
    path('register/html', views.sign_up_by_html, name='register_html'),
]
