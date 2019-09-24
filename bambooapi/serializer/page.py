'''
Created on 2019/09/24

@author: satoukentadashi
'''
from rest_framework import serializers

from bamboo.models.page import Page
from bambooapi.serializer.user import UserSerializer
# from bambooapi.serializer.note import NoteSerializer

class PageSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
#     notes = NoteSerializer(many=True)

    class Meta:
        model = Page
        fields = ('title', 'body', 'status', 'users', 'notes', 'created_at')
        extra_kwargs = {
            'id': {'validators': []},
            'title': {'validators': []},
            'users': {'validators': []}
        }
