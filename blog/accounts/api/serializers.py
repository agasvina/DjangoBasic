import jwt
from django.db.models import Q
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER



UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    email2 = serializers.EmailField(label="Confirm Email",  write_only=True,)
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    #Checking if the email is already exist:
    def validate(self, data):
        email = data['email']
        username = data['username']
        email_qs = UserModel.objects.filter(email=email)
        user_qs = UserModel.objects.filter(username=username)
        if user_qs.exists() or email_qs.exists():
            raise serializers.ValidationError("User has registered")
        return data

    def validate_email2(self, value):
        data = self.get_initial()
        email = data.get("email")
        email2 = value
        if email != email2:
            raise serializers.ValidationError("Emails must match")
        return value

    class Meta:
        model = UserModel
        fields = ("username", "email", "email2", "password")

class UserLoginSerializer(serializers.ModelSerializer):
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField(allow_blank=True, required=False)
    email = serializers.EmailField(label="Email", allow_blank=True, required=False)
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )

    def validate(self, data):
        email = data.get("email", None)
        username = data.get("username", None)
        password = data['password']

        if not email and not username:
            raise serializers.ValidationError("Email or username is required")
        user = UserModel.objects.filter(
            Q(email=email) |
            Q(username=username)
        )

        #Only the users which have email can be authenticated:
        user = user.exclude(email__isnull=True)
        
        if user.exists() and user.count() == 1:
            user = user.first()
        else:
            raise serializers.ValidationError("Username or Email is not valid")
        if user and not user.check_password(password):
            raise serializers.ValidationError("Incorrect credential")

        #TODO: NEED TO BE UPDATED
        user = authenticate(username=username, password=password)
        if not user:
            user = authenticate(email=email, password=password)
        payload = jwt_payload_handler(user)

        data['token'] = jwt_encode_handler(payload)
        return data

    class Meta:
        model = UserModel
        fields = ("username", "email", "password", "token")