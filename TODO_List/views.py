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
    
    
    
def edit(request, todo_id=None, template_name="TODO_List/edit.html"):
    if todo_id:
        todo = get_object_or_404(TODO_Item, pk=todo_id)
    else:
        todo = TODO_Item()

    form = TODO_Item_Form(request.POST or None, instance=todo)
    if request.POST and form.is_valid():
        form.save()

        # Save was successful, so redirect to another page
        return HttpResponseRedirect(reverse('TODO_List:index'))

    return render(request, template_name, { 'form': form, 'todo_id' : todo.id })
    
def delete(request, todo_id):
    todo = get_object_or_404(TODO_Item, pk=todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('TODO_List:index'))