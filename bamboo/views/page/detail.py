'''
Created on 2019/09/15

@author: satoukentadashi
'''
from django.views import generic
from bamboo.models.page import Page
from bamboo.models.page_comment import PageComment

class DetailView(generic.ListView):
    model = PageComment
    paginate_by = 3
    context_object_name = 'page_comments'
    template_name = "bamboo/page/detail.html"

    def get_queryset(self):
        print("bamboo.page_comment.DetailView.get_queryset")
        self.model.objects = self.model.objects.prefetch_related("users")
        self.model.objects = self.model.objects.filter(pages=self.kwargs.get("pk"))
        return self.model.objects.order_by('-created_at')

    def get_context_data(self, **kwargs):
        print("bamboo.page_comment.DetailView.get_context_data")
        context = super(DetailView, self).get_context_data(**kwargs)
        context['page'] = Page.objects.prefetch_related("notes", "users").get(pk=self.kwargs.get("pk"))
        return context
