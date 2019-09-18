'''
Created on 2019/09/12

@author: satoukentadashi
'''
from django.views import generic
from django.db.models import Prefetch
from bamboo.models import Note
from bamboo.models.user import User

class IndexView(generic.ListView):
    model = Note
    queryset = Note.objects.prefetch_related("users")
    paginate_by = 2
    template_name = "bamboo/note/index.html"

    def get_queryset(self):
        print("bamboo.note.IndexView.get_queryset")
        return Note.objects.order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        print("bamboo.note.IndexView.get_context_data")
        context["title"] = "Celaeno"
        return context
#         return render(request, "bamboo/note/index.html", context)