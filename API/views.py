from rest_framework import generics
from DataManagement.models import MetaData
from .serializers import MetaDataSerializer

class MetaDataListCreate(generics.ListCreateAPIView):
    queryset = MetaData.objects.all()
    serializer_class = MetaDataSerializer
