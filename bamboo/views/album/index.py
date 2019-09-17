'''
Created on 2019/09/12

@author: satoukentadashi
'''
from django.views.generic import ListView
class IndexView(ListView):
    template_name = "bamboo/album/index.html"
