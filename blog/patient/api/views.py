from rest_framework.generics import ListAPIView
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view
from rest_framework.response import Response


# from django.db.models import Count, Sum

from .serializers import FollowupModelSerializer
from patient.models import Followup

class FollowupListAPIView(ListAPIView):
    serializer_class = FollowupModelSerializer
    # pagination_class = KaggleLimitOffsetPagination

    def get_queryset(self):
        return Followup.objects.all()