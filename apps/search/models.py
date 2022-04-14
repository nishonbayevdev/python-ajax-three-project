from django.db import models

# Create your models here.
class SearchModel(models.Model):
    title = models.CharField(max_length=128 ,  verbose_name='Sarlavha')
    text = models.TextField(blank=False, verbose_name='Matn')
    createData = models.DateTimeField(auto_now_add=False, verbose_name='Vaqt')
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name_plural = "Qidiruv"
