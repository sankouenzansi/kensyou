from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class weather(models.Model):
    city = models.CharField(max_length=80)
    hi = models.IntegerField()
    lo = models.IntegerField()
    prcp = models.IntegerField()
    date = models.DateField()
