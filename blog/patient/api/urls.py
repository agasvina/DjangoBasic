from django.conf.urls import url
from .views import (
    FollowupListAPIView,
    SurgicalListAPIView,
    MaindataListAPIView,
    HormoneListAPIView,
    RadiotherapyListAPIView,
)

urlpatterns = [
    url(r'^followup/$', FollowupListAPIView.as_view(), name='FUlist'),
    url(r'^surgical/$', SurgicalListAPIView.as_view(), name='SUlist'),
    url(r'^main/$', MaindataListAPIView.as_view(), name='MDlist'),
    url(r'^hormone/$', HormoneListAPIView.as_view(), name='HOlist'),
    url(r'^radio/$', RadiotherapyListAPIView.as_view(), name='RAlist'),
]
