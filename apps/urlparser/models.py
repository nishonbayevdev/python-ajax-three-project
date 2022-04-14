from django.db import models

# Create your models here.
class UrlParser(models.Model):
    url = models.CharField(max_length=1024)
    uuid = models.CharField(max_length=1024)
    class Meta:
        verbose_name_plural= 'Url parser'
    def __str__(self) -> str:
        return self.url
