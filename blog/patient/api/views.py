from rest_framework.generics import ListAPIView
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view
from rest_framework.response import Response


# from django.db.models import Count, Sum

from .serializers import (
    FollowupModelSerializer,
    SurgicalModelSerializer,
    MaindataModelSerializer,
    HormoneModelSerializer,
    RadiotherapyModelSerializer,
)

from patient.models import (
    Followup,
    Surgical,
    Maindata,
    Hormone,
    Radiotherapy,
)

class FollowupListAPIView(ListAPIView):
    serializer_class = FollowupModelSerializer
    # pagination_class = KaggleLimitOffsetPagination

    def get_queryset(self):
        patientID = self.request.GET.get('id')
        if patientID:
            return Followup.objects.filter(patient=patientID)
        return Followup.objects.all()

#TODO: Create for each patient. 

class SurgicalListAPIView(ListAPIView):
    serializer_class = SurgicalModelSerializer

    def get_queryset(self):
        patientID = self.request.GET.get('id')
        if patientID:
            return Surgical.objects.filter(patient=patientID)
        return Surgical.objects.all()


class MaindataListAPIView(ListAPIView):
    serializer_class = MaindataModelSerializer

    def get_queryset(self):
        patientID = self.request.GET.get('id')
        if patientID:
            return Maindata.objects.filter(patient=patientID)
        return Maindata.objects.all()

class HormoneListAPIView(ListAPIView):
    serializer_class = HormoneModelSerializer

    def get_queryset(self):
        patientID = self.request.GET.get('id')
        if patientID:
            return Hormone.objects.filter(patient=patientID)
        return Hormone.objects.all()

class RadiotherapyListAPIView(ListAPIView):
    serializer_class = RadiotherapyModelSerializer

    def get_queryset(self):
        patientID = self.request.GET.get('id')
        if patientID:
            return Radiotherapy.objects.filter(patient=patientID)
        return Radiotherapy.objects.all()
