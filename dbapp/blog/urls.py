from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_list, name='post'),
]
