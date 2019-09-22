'''
Created on 2019/09/15

@author: satoukentadashi
'''
from django.views import generic
from bamboo.models.note import Note
from bamboo.models.page import Page

class DetailView(generic.ListView):
    model = Page
    paginate_by = 3
    context_object_nane = "page_list"
    template_name = "bamboo/note/detail.html"

    def get_queryset(self):
        print("bamboo.note.DetailView.get_queryset")
        self.model.objects = self.model.objects.prefetch_related("notes", "users")
        self.model.objects = self.model.objects.filter(notes=self.kwargs.get("pk"))
        return self.model.objects.order_by('-created_at')

    def get_context_data(self, **kwargs):
        print("bamboo.note.DetailView.get_context_data")
        context = super(DetailView, self).get_context_data(**kwargs)
        context['note'] = Note.objects.get(pk=self.kwargs.get("pk"))
        return context
