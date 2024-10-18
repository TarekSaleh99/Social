from django.urls import path
from . import views



urlpatterns = [
    path('create/', views.post_create, name='create'),
    path('detail/<int:id>', views.post_detail, name='post-detail'),
    path('feed/', views.feed, name='feed'),
    path('like', views.like_post, name='like'),
] 