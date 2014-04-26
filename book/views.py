from django.shortcuts import render
from django import forms
from django.template import RequestContext,Context
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse


# app specific files

from .models import *
from .forms import *



# Create your views here.
def create_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BookForm()

    t = get_template('book/create_book.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))


def list_book(request):
    list_items = Book.objects.all()

    paginator = Paginator(list_items, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        list_items = paginator.page(page)
    except:
        list_items = paginator.page(paginator.num_pages)
    t = get_template("book/list_book.html")
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))



def view_book(request, id):
    book_instance = Book.objects.get(id=id)

    t = get_template("book/view_book.html")
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))
    # context=Context({'book_instance',book_instance})
    # return render(request,"book/view_book.html",context)

def edit_book(request, id):
    book_instance = Book.objects.get(id=id)
    form = BookForm(request.POST or None, instance=book_instance)
    if form.is_valid():
        form.save()
    t = get_template('book/edit_book.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))
