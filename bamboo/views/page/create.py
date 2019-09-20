'''
Created on 2019/09/18

@author: satoukentadashi
'''
from django.urls import reverse_lazy
from django.views.generic import FormView
from bamboo.models.page import Page
from bamboo.models.note import Note
from bamboo.form.page_form import PageForm

class CreateView(FormView):
    model = Page
    form_class = PageForm
    template_name = "bamboo/page/form.html"

    success_url = reverse_lazy("bamboo:note_index")

    def get_initial(self):
        print("bamboo.views.page.create.CreateView.get_initial ")
        initial = super().get_initial()
        initial['users'] = self.request.user
        return initial

    def get_context_data(self, **kwargs):
        print("bamboo.views.page.create.CreateView.get_context_data ")
        context = super(FormView, self).get_context_data(**kwargs)
        print(self.kwargs.get("notes"))
        context['notes'] = Note.objects.get(pk=self.kwargs.get("notes"))
        return context

    def get(self, request, *args, **kwargs):
        print("bamboo.views.page.create.CreateView.get ")
        return FormView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print("bamboo.views.page.create.CreateView.post ")
        print(request.POST)
        page_form = PageForm(request.POST)
        print("bamboo.views.page.create.CreateView.post page_form")
        print(page_form)
        page_form.save()
        return FormView.post(self, request, *args, **kwargs)

    def form_valid(self, form):
        print("bamboo.views.page.create.CreateView.form_valid ")
        return super(CreateView, self).form_valid(form)