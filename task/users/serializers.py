from rest_framework import serializers
from .models import Users



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

        
    def create(self, validated_data):
        user = Users(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user