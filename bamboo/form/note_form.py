'''
Created on 2019/09/18

@author: satoukentadashi
'''
from django import forms
from bamboo.models.note import Note

class NoteForm(forms.ModelForm):
    class Meta():
        model = Note
        fields =('title', 'body', 'status', 'users')
        exclude = ('usernote',)