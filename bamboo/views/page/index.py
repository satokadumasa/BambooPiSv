'''
Created on 2019/09/12

@author: satoukentadashi
'''
from django.views import generic
from bamboo.models import Page

class IndexView(generic.ListView):
    model = Page
    paginate_by = 1
    template_name = "bamboo/page/index.html"

    def get_queryset(self):
        print("bamboo.page.IndexView.get_queryset")
        return Page.objects.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        return context
