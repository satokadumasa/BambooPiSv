'''
Created on 2019/09/24

@author: satoukentadashi
'''
import django_filters
from rest_framework import viewsets, filters

from bamboo.models.note import Note
from bambooapi.serializer.note import NoteSerializer


class NoteIndexViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    paginate_by = 2
    serializer_class = NoteSerializer
