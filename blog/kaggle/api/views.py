from rest_framework.generics import ListAPIView

#We can also set the pagination in the setting
from .pagination import (
	KaggleLimitOffsetPagination,
	# KagglePageNumberPagination,
)
from .serializers import KaggleModelSerializer
from kaggle.models import Sales

class KaggleListAPIView(ListAPIView):
    serializer_class = KaggleModelSerializer
    pagination_class = KaggleLimitOffsetPagination

    def get_queryset(self):
        return Sales.objects.all()