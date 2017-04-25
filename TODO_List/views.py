from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import TODO_Item, TODO_Item_Form

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
    if request.method == 'POST':
        form = TODO_Item_Form(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            return HttpResponseRedirect(reverse('TODO_List:index'))
    else:
        form = TODO_Item_Form()
    
    return render(request, 'TODO_List/new.html', {'form': form})
    
def delete(request, todo_id):
    todo = get_object_or_404(TODO_Item, pk=todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('TODO_List:index'))