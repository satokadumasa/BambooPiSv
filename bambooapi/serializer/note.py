'''
Created on 2019/09/24

@author: satoukentadashi
'''
from rest_framework import serializers

from bamboo.models.note import Note
from bambooapi.serializer.page import PageSerializer
from bambooapi.serializer.user import UserSerializer

class NoteSerializer(serializers.ModelSerializer):
    pages = PageSerializer(many=True)
    users = UserSerializer(many=True)

    class Meta:
        model = Note
        fields = ('title', 'body', 'users', 'pages', 'status', 'created_at')
        extra_kwargs = {
            'id': {'validators': []},
            'title': {'validators': []},
            'users': {'validators': []}
        }
