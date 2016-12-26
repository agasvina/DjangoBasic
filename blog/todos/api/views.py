from django.db.models import Q

from rest_framework.filters import (
	# SearchFilter,
	OrderingFilter,
)

from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination,
)

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

from rest_framework.mixins import (
	DestroyModelMixin,
	UpdateModelMixin,
)

from todos.models import Todo

from .serializers import (
	TodoDetailSerializer,
	TodoListSerializer,
	TodoCreateSerializer,
)
from .permissions import IsOwnerOrReadOnly

class TodoListAPIView(ListAPIView):
    serializer_class = TodoListSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [OrderingFilter]
    # search_fields = ['todo',]

    def get_queryset(self, *args, **kwargs):
    	queryset_list = Todo.objects.all()
    	query = self.request.GET.get('q')
    	if query:
    		queryset_list = queryset_list.filter(
    			Q(todo__icontains=query),
    		)
    	return queryset_list

class TodoDetailAPIView(RetrieveAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoDetailSerializer
	#To Specify the lookup field:
	# lookup_field = ''


class TodoCreateAPIView(CreateAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoCreateSerializer
	permission_classes = [IsAuthenticated]

	def perform_create(self, serializer):
	    serializer.save(user=self.request.user)

class TodoUpdateAPIView(UpdateAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoDetailSerializer
	permission_classes = [IsOwnerOrReadOnly]

class TodoDeleteAPIView(DestroyAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoDetailSerializer

class TodoEditDeleteAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
	queryset = Todo.objects.all()
	serializer_class = TodoDetailSerializer

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)
