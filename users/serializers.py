from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nome', 'email']

    def create(self, validated_data):
        return User.objects.create(**validated_data)
