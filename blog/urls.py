from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('contacts/', views.contacts, name = 'blog-contacts')
]
