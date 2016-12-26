from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)

from todos.models import Todo

class TodoCreateSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id',
            'todo',
            'category',
            'completed',
            'created',
        ]

class TodoListSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id',
            'todo',
            'category',
            'completed',
            'created',
        ]

class TodoDetailSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = [
            'id',
            'todo',
            'category',
            'completed',
            'created',
        ]

class TodoListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name = 'todo-api:detail',
        lookup_field='pk',
    )
    user = SerializerMethodField()

    class Meta:
        model = Todo
        fields = [
            'url',
            'user',
            'todo',
            'category',
            'completed',
            'created',
        ]

    def get_user(self, obj):
        return str(obj.user.username)