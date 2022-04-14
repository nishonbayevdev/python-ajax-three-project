from django.http import HttpResponse, JsonResponse 
from django.shortcuts import render , redirect
from .models import ToDoList
from django.utils.timezone import datetime , timedelta
# Create your views here.
def index (request):
    context = {
        'lists':ToDoList.objects.all()
    }
    return render(request , 'todo-list.html' , context)
def DeleteList(request , pk):
    listData = ToDoList.objects.get(id=pk)
    listData.delete()
    return redirect("index")


def addList(request):
    if request.method == "POST":
        print(request.POST['work'])
        toDoList = ToDoList(
            work=request.POST['work'],
            startTime = datetime.now(),
            finsihTime = str(timedelta(hours=datetime.now().hour + 1 , minutes=datetime.now().minute))
        ) 
        toDoList.save()
        data = ToDoList.objects.all()
        print(list(data))
        print(Serializer(list(data)))
        return JsonResponse({"data":Serializer(list(data))})
        # {
        #     "id":data.id,
        #     "work": data.work,
        #     "sTime":data.startTime,
        #     "fTime":data.finsihTime,
        # }
def Serializer(ListData : list):
    JsonList = []
    for listData in ListData:
        if listData is not [] and listData is not None:
            json = {
                    "id":listData.id,
                    "work": listData.work,
                     "sTime":listData.startTime,
                     "fTime":listData.finsihTime,
                }
            JsonList.append(json)
    return JsonList