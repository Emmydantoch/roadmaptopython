from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, this is the index view, <h1>This is the about page.</h1><p>Welcome to the about page of our website.</p>")

def index(request):
    return render(request, 'index.html')