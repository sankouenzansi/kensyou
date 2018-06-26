# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.db import connection

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def select(request):
    return HttpResponse("test")

def get_connection(self):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM weather;"
        cursor.execute(sql)
        results =cursor.fetchall()
    return HttpResponse(results)


