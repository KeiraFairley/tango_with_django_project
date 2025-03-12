from django.shortcuts import render
from django.http import HttpResponse
from tango_with_django_project import settings
 

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return render(request, 'rango/about.html', {'MEDIA_URL': settings.MEDIA_URL})