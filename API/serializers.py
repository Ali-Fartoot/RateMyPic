from rest_framework import serializers
from DataManagement.models import MetaData

class MetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaData
        fields = '__all__'
