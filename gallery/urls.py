from django.urls import path
from . import views

urlpatterns = [
    path('like_image/<int:image_id>/', views.like_image, name='like_image'),
    path('dislike_image/<int:image_id>/', views.dislike_image, name='dislike_image'),
    path('', views.image_gallery, name='image_gallery'),
]