from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages

from .forms import TodoForm
from .models import Todo

# from django.http import HttpResponse
# from django.shortcuts import render, get_object_or_404



def index(request):
 
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()
 
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)
 
 
### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    # item = get_object_or_404(Todo, id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')

### function to update item, it receive todo item_id as primary key from url ##
def update(request, item_id):
    todo_item = get_object_or_404(Todo, id=item_id)

    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo_item)
        if form.is_valid():
            form.save()
            messages.success(request, "Item updated successfully!")
            return redirect('todo')
    else:
        form = TodoForm(instance=todo_item)
 
    page = {
        "forms": form,
        "list": Todo.objects.order_by("-date"),
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)

# def login(request):

# def update(request, item_id):
#     item = Todo.objects.get(id=item_id)
#     if request.method == 'POST':
#         item = request.form['new_content']
#         Todo.content = item
#         item.save()
#     return redirect('todo')

