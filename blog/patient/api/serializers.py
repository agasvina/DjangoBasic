from rest_framework import serializers
from patient.models import Followup

class FollowupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Followup
        fields = [
            'patient',
            'fudate'
        ]