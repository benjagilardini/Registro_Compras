from django.db import models
from django.conf import settings

# Create your models here.

class Tabla(models.Model):
	datetime = models.DateTimeField('Fecha',auto_now=True)
	compra = models.CharField(max_length = 50)








