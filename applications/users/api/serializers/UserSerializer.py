from rest_framework import serializers
from applications.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email',
                  'first_name', 'gender',
                  'password']

    def to_representation(self, instance):
        return {
            "user_name": instance.username,
            "user_lastname": instance.first_name
        }

    def validate_username(self, value):
        if value is None:
            raise serializers.ValidationError('The field cannot be empty')
        if len(value) < 8:
            raise serializers.ValidationError('more than 8 characters')
        return value

    def validate_first_name(self, value):
        if value is None:
            raise serializers.ValidationError('The field cannot be empty')
        return value

    def validate_password(self, value):
        if value is None:
            raise serializers.ValidationError('The field cannot be empty')
        return value

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
