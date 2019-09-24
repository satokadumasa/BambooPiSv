'''
Created on 2019/09/23

@author: satoukentadashi
'''
'''
Created on 2019/09/23

@author: satoukentadashi
'''
from rest_framework import serializers
from bamboo.models.note import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('name', 'mail')
