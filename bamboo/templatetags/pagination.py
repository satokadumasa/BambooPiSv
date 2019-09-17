'''
Created on 2019/09/14

@author: satoukentadashi
'''
from django import template

register = template.Library()

@register.simple_tag
def query_pagination(request, page_number):
    #request.GETの値コピー
    querydict = request.GET.copy()
    #ページ情報を代入 # Django2.1対策。通常はvalueだけでOK
    querydict['page'] = str(page_number)
    #ページに関するクエリ生成
    #htto://~?以下の検索クエリを返す
    return querydict.urlencode()
