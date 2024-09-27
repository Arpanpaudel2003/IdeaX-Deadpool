from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('map/', views.map),
    path('translate/', views.translate, name='translate'),
]