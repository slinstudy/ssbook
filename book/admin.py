from django.contrib import admin

# Register your models here.
from .models import *


class BookAdmin(admin.ModelAdmin):
    list_display = ('id','isbn', 'title', 'author', 'publisher', 'pubdate')


admin.site.register(Book,BookAdmin)