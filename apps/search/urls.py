from django.urls import re_path,path
from .views import index
from .views import Search
from .views import PostRead
urlpatterns = [
    re_path(r'^$' , index , name='index'),
    path('search/' , Search , name='search'),
    path('post/<int:id>/' , PostRead , name='post')
]