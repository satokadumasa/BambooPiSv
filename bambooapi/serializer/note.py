'''
Created on 2019/09/24

@author: satoukentadashi
'''
from rest_framework import serializers

from bamboo.models.note import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('title', 'body', 'users', 'pages', 'status', 'created_at')
