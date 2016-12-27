from rest_framework.generics import ListAPIView
from rest_framework.status import HTTP_200_OK
from rest_framework.decorators import api_view
from rest_framework.response import Response


from django.db.models import Count, Sum

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

@api_view(['GET'])
def total_games(request):
    form = request.query_params.get('form')
    sales = [x for x in Sales.objects.values('platform').annotate(total=Count('platform')).all()]
    if form == 'd3':
        res = []
        res.append({
            "key": "Total Sales",
            "values": sales
        })
        return Response(res, status=HTTP_200_OK)
    return Response(sales, status=HTTP_200_OK)

@api_view(['GET'])
def get_sales_summary(request):
    temp = {}
    region = request.query_params.get('region')
    platforms = request.GET.getlist('platform', '')
    form = request.query_params.get('form')

    if not region:
        region = 'global_sales'
    result_qs = None
    if type(platforms) is list and len(platforms) > 0:    
        result_qs = Sales.objects.filter(platform__in =platforms).values('platform','year_of_release').annotate(
                        sales = Sum(region),).all() 
    else:
        result_qs = Sales.objects.values('platform','year_of_release').annotate(
                        sales = Sum(region),).all() 
    if form == 'd3':
        res = [helper(temp, x) for x in result_qs]
        return Response(temp.values(), status=HTTP_200_OK)
    else:
        res = [x for x in result_qs]
        return Response(res, status=HTTP_200_OK)

def helper(temp, data):
    key = data['platform']
    if key not in temp:
        temp[key] = {
            "key": key,
            "values": []
        }
    if data['year_of_release'] > 0:
        temp[key]['values'].append({
            'x': data['sales'],
            'y': data['year_of_release'],
        })

