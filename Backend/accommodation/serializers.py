from rest_framework import serializers
from accommodation.models import AccommodationRequest
from django.contrib.auth.models import User


class AccommodationRequestSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = AccommodationRequest
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    accommodation_requests = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=AccommodationRequest.objects.all(),
    )

    class Meta:
        model = User
        fields = "__all__"


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
