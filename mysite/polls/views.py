# Create your views here.
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.db import connection

from sqlalchemy import create_engine
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.sql import select

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

#生SQL有
def get_connection(self):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM weather;"
        cursor.execute(sql)
        results =cursor.fetchall()
    return HttpResponse(results)

#生SQLなし(SQLAlchemy有)
def get_connection2(self):
    url = 'postgresql://postgres:postgres@127.0.0.1:5432/testdb'
    engine = create_engine(url)
    conn = engine.connect()
    metadata = MetaData()
    users = Table('users', metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('fullname', String),
    )
    s = select([users])
    result = conn.execute(s) 
    return HttpResponse(result)
