from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    user = serializers.CharField(required=True)
    password = serializers.CharField(required=True)