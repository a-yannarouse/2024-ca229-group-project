# simple_test_root/pages/views.py
from django.shortcuts import render
from .models import Page

def index(request, pagename=''):
    pagename = '/' + pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
        'pagename': pg.title,
    }
    return render(request, 'pages/page.html', context)
