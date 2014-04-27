from django.contrib import admin

# Register your models here.
from .models import *


class BookAdmin(admin.ModelAdmin):
    # list_display = ('id','isbn', 'title', 'author', 'publisher', 'pubdate')
	list_display = ('id','isbn', 'title', 'author','translator','publisher',)
	list_filter = ('publisher',)
	search_fields = ('id','title','isbn',)
	list_per_page=20

admin.site.register(Book,BookAdmin)