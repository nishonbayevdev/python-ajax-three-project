from turtle import title
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import SearchModel

# Create your views here.
def index(request):
    context = {
        'Data' : SearchModel.objects.all()
    }
    return render(request , 'search.html' , context)
def Search(request):
    if request.method == "GET":
        print(request.GET)
        key = request.GET['search']
        dataBase = ""
        if key != "":
            dataBase = SearchModel.objects.filter(title__contains = key)
            if len(dataBase) != 0:
                dataBase = JsonResponseChange(list(dataBase))
            else :
                dataBase = []
        else :
            dataBase = ""
        return JsonResponse({'data' : dataBase})
def PostRead(request , id):
    context = {
        'data' : SearchModel.objects.get(id = id)
    }
    return render(request , 'post-read.html' , context)
def JsonResponseChange(Data:list) -> list:
    newJson = []
    for data in Data:
        newJson.append(
            {  
                'id' : data.id,
                'title' : data.title,
                'text' : data.text,
                'time' : data.createData
            }
        )
    return newJson

