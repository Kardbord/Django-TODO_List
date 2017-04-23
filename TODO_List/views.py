from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import TODO_Item

# Create your views here.

# TODO: create an edit view with pattern like .../home/[pk]/edit if time

# home will need options to add, delete, or mark TODO items as complete
def index(request):
    todo_list = TODO_Item.objects.order_by('due_date')
    context = {
        'todo_list': todo_list,
    }
    return render(request, 'TODO_List/index.html', context)
    
    
    
def detail(request, todo_id):
    todo_item = get_object_or_404(TODO_Item, pk=todo_id)
    return render(request, 'TODO_List/detail.html', {'todo_item': todo_item})
    
    
    
def new(request):
    return render(request, 'TODO_List/new.html')