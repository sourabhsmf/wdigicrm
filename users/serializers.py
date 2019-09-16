from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password' , 'date_joined')

    def create(self, validated_data):
        password = validated_data.pop('password')
        userCreated = User.objects.create(**validated_data)
        userCreated.set_password(password)
        userCreated.save()
        return userCreated
    def update(self, instance ,validated_data):
        password = validated_data.get("password", instance.password)
        instance.username = validated_data.get("username", instance.username)
        instance.set_password(password)
        instance.save()
        return instance