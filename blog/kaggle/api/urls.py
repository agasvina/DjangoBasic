from django.conf.urls import url
from .views import (
    KaggleListAPIView
)

urlpatterns = [
    url(r'^$', KaggleListAPIView.as_view(), name='list'),
]
