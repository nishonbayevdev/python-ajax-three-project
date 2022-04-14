import uuid
from django.http import HttpResponse
from django.shortcuts import redirect, render
from uuid import uuid4
from .models import UrlParser
# Create your views here.
def index(request):
    context = {
        
    }
    return render(request , 'url-parser.html' , context)

def make(request):
    if request.method == "POST":
        url = request.POST["generate"]
        address = str(uuid4())[:6]
        data = UrlParser(url=url , uuid = address)
        data.save()
        return HttpResponse(address)
def parser(request , pk ) :
    print(pk)
    url = UrlParser.objects.get(uuid = pk)
    return redirect(url.url)