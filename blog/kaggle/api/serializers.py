from rest_framework import serializers
from kaggle.models import Sales

class KaggleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = [
            'name',
            'platform'
        ]