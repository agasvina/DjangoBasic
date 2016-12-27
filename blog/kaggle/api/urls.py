from django.conf.urls import url
from .views import (
    KaggleListAPIView,
    total_games,
    get_sales_summary,
)

urlpatterns = [
    url(r'^$', KaggleListAPIView.as_view(), name='list'),
    url(r'^total/$', total_games, name='total'),
    url(r'^summary/$', get_sales_summary, name='summary'),
]
