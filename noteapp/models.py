from django.db import models


# Create your models here.
class Notes(models.Model):
    Name = models.CharField(max_length=30, unique=True)


class Items(models.Model):
    task = models.CharField(max_length=30, unique=True)
    Note_id = models.ForeignKey(Notes, related_name='items',default=1,on_delete=models.CASCADE)