from django.urls import re_path , path
from .views import index
from .views import addList
from .views import DeleteList
urlpatterns = [
    re_path(r'^$' , index , name='index'),
    re_path(r'^add/$' , addList , name='add'),
    path(r'delete/<int:pk>/one/' , DeleteList , name='delete')
]