'''
Created on 2019/09/15

@author: satoukentadashi
'''
from django.views import generic
from bamboo.models import Note


class DetailView(generic.DetailView):
    model = Note
    queryset = Note.objects.prefetch_related("pages__users", "users")
    context_object_name = 'note'
    template_name = "bamboo/note/detail.html"
