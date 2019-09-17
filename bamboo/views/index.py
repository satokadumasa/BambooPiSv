'''
Created on 2019/09/12

@author: satoukentadashi
'''
from django.views.generic import TemplateView
class IndexView(TemplateView):
    template_name = "bamboo/index.html"