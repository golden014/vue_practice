from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ['id', 'name', 'email', 'password', 'username']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    #override create
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            #set password akan nge hash password
            instance.set_password(password)
        instance.save()

        return instance