from django.urls import path
from .views import MetaDataListCreate

urlpatterns = [
    path('post/', MetaDataListCreate.as_view(), name='data-list-create'),
]
