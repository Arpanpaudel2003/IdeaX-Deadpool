from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home,name = ''),
    path('map/', views.map, name='map'),
    path('currency/', views.currency, name='currency'),
    path('blog/', views.blog, name='blog'), 
    path('blog/update/<int:pk>/', views.updatePost, name='update_post'),
    path('blog/delete/<int:pk>/', views.deletePost, name='delete_post'), 
    path('translate/', views.translate, name='translate')
=======
    path('', views.home),
    path('map/', views.map),
    path('translate/', views.translate, name='translate'),
>>>>>>> a32c93576d72888ee63409c5195eb2624417066e
]