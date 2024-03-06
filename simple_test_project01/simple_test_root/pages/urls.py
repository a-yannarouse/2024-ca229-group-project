# simple_test_root/pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('<str:pagename>/', views.index, name='index'),
    path('', views.index, name = 'index'),
]
