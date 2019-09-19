'''
Created on 2019/09/15

@author: satoukentadashi
'''
from django.views import generic
from bamboo.models.page import Page

class DetailView(generic.DetailView):
    model = Page
    queryset = Page.objects.prefetch_related("users", "page_comments__users")
    context_object_name = 'page'
    template_name = "bamboo/page/detail.html"
