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
    min_year = request.query_params.get('min_year')
    max_year = request.query_params.get('max_year')
    platforms = request.GET.getlist('platform', '')
    form = request.query_params.get('form')

    if not region:
        region = 'global_sales'
    result_qs = None
    if type(platforms) is list and len(platforms) > 0:    
        result_qs = Sales.objects.filter(platform__in =platforms).values('platform','year_of_release').annotate(
                        sales = Sum(region),).all() 
    else:
        platforms = [x['platform']  for x in Sales.objects.values('platform').distinct().all()]
        result_qs = Sales.objects.values('platform','year_of_release').annotate(
                        sales = Sum(region),).all() 
    if form == 'd3':    
        #We need to clean the data:
        pl = {}
        result = {}
        for platform in platforms:
            pl[platform] = {}
            for x in range(int(min_year),int(max_year)+1):
                pl[platform][str(x)] = False;
        res = [helper(temp, x, pl) for x in result_qs]
        #Clean data:
        for platform in platforms:
            result[platform] = {
                "key": platform,
                "values": []
            }
            for x in range(int(min_year),int(max_year)+1):
                if pl[platform][str(x)] == False:
                    result[platform]['values'].append({
                        'y': 0,
                        'x': x,
                    })
                else:
                    result[platform]['values'].append({
                        'y': temp[platform][str(x)],
                        'x': x,
                    })
        return Response(result.values(), status=HTTP_200_OK)
    else:
        res = [x for x in result_qs]
        return Response(res, status=HTTP_200_OK)

def helper(temp, data, pl):
    key = data['platform']
    year = data['year_of_release']
    if key not in temp:
        temp[key] = {}
    if year > 0:
        pl[key][str(year)]= True
        temp[key][str(year)] = data['sales']

