# simple_t<int:num1>/<int:num2>/<int:num3>/est_root/pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('<str:pagename>/', views.index, name='index'),
    path('magic/<int:num1>/<int:num2>/<int:num3>/', views.magic_page, name='magic'),
    path('', views.index, name = 'index'),
]