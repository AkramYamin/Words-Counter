from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'name':'akram', })


def count(request):
    dictionary = {}
    fulltext = request.GET['full-text']
    words = fulltext.split()
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return render(request, 'count.html', {'fulltext':fulltext, 'words':dictionary.items()})


def about(request):
    return render(request, 'about.html')
