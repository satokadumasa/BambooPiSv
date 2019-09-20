'''
Created on 2019/09/18

@author: satoukentadashi
'''
from django import forms
from bamboo.models.page import Page

class PageForm(forms.ModelForm):
    class Meta():
        model = Page
        fields =('title', 'body', 'status', 'users', 'notes')
        exclude = ('notepage', 'usernote',)
