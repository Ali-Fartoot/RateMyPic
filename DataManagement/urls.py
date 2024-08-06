from .views import upload_success, upload_image
from django.urls import path, include

urlpatterns = [
    path('', upload_image, name='upload_image'),
    path('success/', upload_success, name='success_url'),

]
