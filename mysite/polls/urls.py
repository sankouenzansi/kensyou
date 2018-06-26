from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('selects/', views.select, name='selects'),
    path('get_connection/', views.get_connection, name='get_connection'),
]
