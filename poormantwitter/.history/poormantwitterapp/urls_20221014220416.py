
# import views and path
from django.urls import path
from . import views

app_name = 'poormantwitterapp'

urlpatterns = [
     path('', views.index, name='index'),
     path('tweets/', views.tweets, name='tweets'),
     path('savetweet/', views.save_tweet, name='save_tweet'),
]
