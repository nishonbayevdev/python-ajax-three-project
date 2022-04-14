from django.urls import re_path,path
from .views import index
from .views import make
from .views import parser
urlpatterns = [
    re_path(r'^$' , index , name='index'),
    re_path(r'^make/$' , make , name='make'),
    path('<str:pk>/' , parser , name='parser')
]