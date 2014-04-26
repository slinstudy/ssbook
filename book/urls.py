from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
	(r'book/create/$', create_book),
	(r'book/list/$', list_book ),
	(r'book/edit/(?P<id>[\d]+)/$', edit_book),
	(r'book/view/(?P<id>[\d]+)/$', view_book), 
)
