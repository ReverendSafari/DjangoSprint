from django.urls import path
from . import views

# URL's needed for the project
urlpatterns = [
    path('register/', views.register, name='register'), #Registration Page
    path('', views.home, name='home'), #Home page (With posts)
    path('post/new/', views.new_post, name='new_post'), #New post form page
    path('post/<int:post_id>/like/', views.like_post, name='like_post'), #Url to like a post (Links to view to handle logic)
]