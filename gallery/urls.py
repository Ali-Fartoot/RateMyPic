from django.urls import path
from . import views

urlpatterns = [
    path('', views.image_gallery, name='gallery'),
    path('like_image/<str:image_id>/', views.like_image, name='like_image'),
    path('dislike_image/<str:image_id>/', views.dislike_image, name='dislike_image'),

]

