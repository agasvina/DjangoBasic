from django.db.models import Q
from django.contrib.auth import get_user_model

# from rest_framework.pagination import (
#   LimitOffsetPagination,
#   PageNumberPagination,
# )

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

#Import Mixin:
# from rest_framework.mixins import (
#   DestroyModelMixin,
#   UpdateModelMixin,
# )

from .serializers import (
    UserSerializer,
    UserLoginSerializer,
)

class UserCreateAPIView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer

class UserLoginAPIView(APIView):
    permission_classes = [
        AllowAny,
    ]
    #If we don't include the serializer class, we only get
    # the raw data
    serializer_class= UserLoginSerializer


    #Because we are using the base API view, 
    #We need to define the method we are using 
    #This is a REST API response
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer= UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.error, status=HTTP_400_BAD_REQUEST)