from django.db import models
from django.utils.timezone import datetime , timedelta

# Create your models here.
class ToDoList(models.Model):
    work = models.CharField(max_length=128)
    startTime = models.TimeField(auto_now_add=False , default= datetime.now(), blank=False)
    finsihTime = models.TimeField(auto_now_add=False , blank=False)
    class Meta:
        verbose_name_plural = "ToDo List"
    def __str__(self) -> str:
        return self.work
