from  rest_framework import serializers
from .models import User

class U_SER(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['photo', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
class User_Get(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['photo', 'username']