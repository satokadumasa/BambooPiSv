"""BambooPiSv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from bamboo.views.index import IndexView
from bamboo.views.note.index import IndexView as NoteIndexView
from bamboo.views.note.detail import DetailView as NoteDetailView
from bamboo.views.note.create import CreateView as NoteCreateView
from bamboo.views.page.index import IndexView as PageIndexView
from bamboo.views.page.detail import DetailView as PageDetailView
from bamboo.views.page.create import CreateView as PageCreateView
from bamboo.views.page_comment.create import CreateView as PageCommentCreateView

app_name = 'bamboo'

urlpatterns = [
    # トップ画面（一覧画面）
    path('', IndexView.as_view(), name='index'),
    # Note一覧画面
    path('note/', NoteIndexView.as_view(), name='note_index'),
    # Note詳細画面
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    # Note新規登録
    path('note/create/', NoteCreateView.as_view(), name='note_create'),
    # 詳細画面
    path('page/', PageIndexView.as_view(), name='page_index'),
    # Page詳細画面
    path('page/<int:pk>/', PageDetailView.as_view(), name='page_detail'),
    # Page新規登録画面
    path('note/<int:notes>/page/create', PageCreateView.as_view(), name='page_crete'),
    # PageComment
    path('page/<int:pages>/page_comment/create', PageCommentCreateView.as_view(), name='page_comment_crete'),

]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns

