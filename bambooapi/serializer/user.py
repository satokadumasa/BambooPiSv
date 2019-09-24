'''
Created on 2019/09/24

@author: satoukentadashi
'''
from rest_framework import serializers
from bamboo.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')
        extra_kwargs = {
            'id': {'validators': []},
            'username': {'validators': []},
            'email': {'validators': []},
        }
