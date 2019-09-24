from django.db import models

# Create your models here.
class main (models.Model):
    id = models.AutoField(primary_key=True)
    status = models.BooleanField('Status', default=True)
    create_date = models.DateField('Creation date', auto_now=False, auto_now_add=True)
    ###.....