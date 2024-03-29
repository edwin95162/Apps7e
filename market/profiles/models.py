from django.db import models
from django.utils import timezone

class Question(models.Model):  # es igual a table question
    question_text = models.CharField(max_length=200) #tipo varchar con 200 espacios
    pub_date = models.DateTimeField('date published') #
    def __str__(self):
        return self.question_text
    def __str__(self):
        return self.pub_date


class Choice(models.Model): # = Create table choice
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #foranea para conectar
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class User(models.Model): # = Create table user
    user_text = models.CharField(max_length=200)
    create = models.DateTimeField('date published')

