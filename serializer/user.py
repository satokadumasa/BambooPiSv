'''
Created on 2019/09/23

@author: satoukentadashi
'''
from rest_framework import serializers
from bamboo.models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')
