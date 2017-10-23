from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	usuario = models.CharField(max_length=100)
	senha = models.CharField(max_length=100)

class Post(models.Model):
	post_id = models.AutoField(primary_key=True)
	autor = models.CharField(max_length=200,default='')
	especie = models.CharField(max_length=200,default='')
	bioma = models.CharField(max_length=200,default='')
	descricao = models.TextField(default='')#CharField(max_length=200)
	votes = models.IntegerField(default=0)
	local = models.TextField(default='')
	published_date = models.DateTimeField(default=timezone.now())
	#picture = models.ImageField(upload_to = 'pictures')
	imagem = models.FileField(null=True, blank=True)
	#class Meta:
    #  db_table = "Post"


