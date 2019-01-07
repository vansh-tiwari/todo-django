from django.shortcuts import render
from polls.models import ToDo

# Create your views here.

def index(request):
    # form = ToDoForm(request.POST or None)

#FOR DIRECT MODEL SAVING
    todoin = ToDo.objects.all()

    if request.method == 'POST':
        if 'taskadd' in request.POST:
            items = request.POST['taskin']
            Todo = ToDo(item = items)
            Todo.save()

        if 'delete' in request.POST:
            items = request.POST['delete']
            todoid = ToDo.objects.filter(item__contains=items)
            todoid.delete()
#FOR FORM
    # todoin = ""
    # if form.is_valid():
    #     todoin = form.cleaned_data.get("task_input")
    #     form.save(commit=true)

    context = {"todoin":todoin}
    return render(request, 'first.html',context)
