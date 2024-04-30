from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('post/new/', views.new_post, name='new_post'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
]