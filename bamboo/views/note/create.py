'''
Created on 2019/09/18

@author: satoukentadashi
'''
from django.urls import reverse_lazy
from django.views.generic import FormView
from bamboo.models.note import Note
from bamboo.form.note_form import NoteForm
from bamboo import templatetags
from bamboo.form import note_form

class CreateView(FormView):
    model = Note
    form_class = NoteForm
    template_name = "bamboo/note/form.html"

    success_url = reverse_lazy("bamboo:note_index")

    def get_initial(self):
        initial = super().get_initial()
        initial['users'] = self.request.user
        return initial

    def get(self, request, *args, **kwargs):
        return FormView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        note_form = NoteForm(request.POST)
        note_form.save()
        return FormView.post(self, request, *args, **kwargs)

    def form_valid(self, form):
        return super(CreateView, self).form_valid(form)