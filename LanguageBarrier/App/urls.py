from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name = ''),
    path('map/', views.map, name='map'),
    path('currency/', views.currency, name='currency'),
    path('blog/', views.blog, name='blog'), 
    path('blog/update/<int:pk>/', views.updatePost, name='update_post'),
    path('blog/delete/<int:pk>/', views.deletePost, name='delete_post'), 
    path('translate/', views.translate, name='translate'),
    path('weather/', views.weather, name = 'weather'),
    path('places/',views.places,name = 'places'),
    path('places/guides.html', views.guides)
   
]