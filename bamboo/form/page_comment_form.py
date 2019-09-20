'''
Created on 2019/09/21

@author: satoukentadashi
'''
from django import forms
from bamboo.models.page_comment import PageComment

class PageCommentForm(forms.ModelForm):
    class Meta():
        model = PageComment
        fields =('title', 'body', 'status', 'users', 'pages')
        exclude = ('notepage', 'usernote',)
