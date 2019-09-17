'''
Created on 2019/09/11

@author: satoukentadashi
'''
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
]
