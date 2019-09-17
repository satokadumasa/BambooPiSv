'''
Created on 2019/09/15

@author: satoukentadashi
'''
from django.views import generic
from bamboo.models import Note


class DetailView(generic.DetailView):
    model = Note
    context_object_name = 'node_detail'
    template_name = "bamboo/note/detail.html"
