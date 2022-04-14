from django.contrib import admin
from .models import SearchModel

# Register your models here.
class SearchAdmin(admin.ModelAdmin):
    list_display = ('title' , 'text' , 'createData')
admin.site.register(SearchModel)
