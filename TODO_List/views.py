from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# TODO: create an edit view with pattern like .../home/[pk]/edit if time

# home will need options to add, delete, or mark TODO items as complete
def home(request):
    return HttpResponse("Hello world! You're at the TODO homepage.")
    
def detail(request, todo_id):
    return HttpResponse("You are looking at todo item number %s." % todo_id)
    
def new(request):
    return HttpResponse("You are adding a todo entry")