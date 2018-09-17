from django.shortcuts import render, redirect
from .models import TodoList, Priority


def index(request):  # the index view
    todos = TodoList.objects.all()  # quering all todos with the object manager
    priorities = Priority.objects.all()  # getting all categories with object manager
    if request.method == "POST":  # checking if the request method is a POST
        if "taskAdd" in request.POST:  # checking if there is a request to add a todo
            title = request.POST["description"]  # title
            priority = request.POST["priority_select"]  # Priority
            content = title + " -- " + priority  # content
            Todo = TodoList(title=title, content=content,
                            priority=Priority.objects.get(name=priority))
            Todo.save()  # saving the todo
            return redirect("/")  # reloading the page
        if "taskDelete" in request.POST:  # checking if there is a request to delete a todo
            # checked todos to be deleted
            checkedlist = request.POST["checkedbox"]
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))  # getting todo id
                todo.delete()  # deleting todo
    return render(request, "index.html", {"todos": todos, "priorities": priorities})
