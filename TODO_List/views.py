from django.shortcuts import render
from django.http import HttpResponse

from .models import TODO_Item

# Create your views here.

# TODO: create an edit view with pattern like .../home/[pk]/edit if time

# home will need options to add, delete, or mark TODO items as complete
def index(request):
    todo_list = TODO_Item.objects.order_by('-due_date')
    context = {
        'todo_list': todo_list,
    }
    return render(request, 'TODO_List/index.html', context)
    
def detail(request, todo_id):
    return HttpResponse("You are looking at todo item number %s." % todo_id)
    
def new(request):
    return HttpResponse("You are adding a todo entry")