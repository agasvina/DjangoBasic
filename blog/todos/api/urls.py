from django.conf.urls import url
from django.contrib import admin

from .views import (
    TodoListAPIView,
    TodoDetailAPIView,
    # TodoUpdateAPIView,
    TodoEditDeleteAPIView,
    TodoDeleteAPIView,
    TodoCreateAPIView,
)

urlpatterns = [
    url(r'^$', TodoListAPIView.as_view(), name='list'),
    url(r'^create/$', TodoCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', TodoDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', TodoEditDeleteAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', TodoDeleteAPIView.as_view(), name='delete'),
]
