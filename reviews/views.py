from django.shortcuts import render
from django.http import HttpResponse

def indexView(request):
    name = request.GET.get('name') or 'worldd'
    design = request.GET.get('design') or 'User'
    # return HttpResponse('hello {}:{}'.format(design, name))
    # name = 'chandr kumar sahu'
    return render(request, 'reviews/base.html', {"name":name, "design":design})

def search_book(request):
    name = request.GET.get('name') or 'default_book'
    return render(request, 'reviews/searchResult.html', {"search_book":name})


