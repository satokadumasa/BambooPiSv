'''
Created on 2019/09/24

@author: satoukentadashi
'''
import django_filters
from rest_framework import viewsets, filters

from bamboo.models.note import Note
from bambooapi.serializer.note import NoteSerializer


class NoteIndexViewSet(viewsets.ModelViewSet):
    model = Note
    queryset = model.objects.prefetch_related('pages__users', "users")
    paginate_by = 2
    serializer_class = NoteSerializer
