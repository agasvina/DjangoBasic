from django.conf.urls import url
from .views import (
    FollowupListAPIView,
)

urlpatterns = [
    url(r'^followup/$', FollowupListAPIView.as_view(), name='list'),
]
