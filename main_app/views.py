from typing import Text
from django.shortcuts import render
from .models import Todo
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    context = {
        'todo_items': todo_items,
    }
    return render(request,'main/index.html',context)

@csrf_exempt
def add_todo(request):
    added_date = timezone.now()
    content = request.POST['content']
    created_obj = Todo.objects.create(added_date=added_date,text = content)
    # print(created_obj)
    # print(created_obj.id)
    length_of_todo = Todo.objects.all().count
    return HttpResponseRedirect('/')     

@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id = todo_id).delete()
    return HttpResponseRedirect("/")