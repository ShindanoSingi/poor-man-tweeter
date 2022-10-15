from django.utils import timezone
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tweet


# Create your views here.
def index(request):
     return render(request, 'poormantwitterapp/index.html')

# get all tweets ==> this is basically a GET request.
def tweets(request):

     # Order data by author name and date.
     tweet_items = Tweet.objects.order_by("author", "date")

     # Create a dictionary to hold all the tweets.
     data = {
          'tweet_items':[]
     }

     # Loop through all the tweets and add them to the dictionary.
     for tweet_item in tweet_items:
          data['tweet_items'].append({
               'author': tweet_item.author,
               'body': tweet_item.body,
               'date': tweet_item.date,
          })

     return JsonResponse(data)

def save_tweet(request):

     data = json.loads(request.body)

     author_text = data['author_text']
     body_text = data['body_text']

     # Ensure both author input text and body text have data before saving to the database.
     if ((len(author_text) > 0) and (len(body_text) > 0)):

          # Capture the new tweet object to the database
          tweet_item = Tweet(author=author_text, body=body_text, date=timezone.now())

          # Save input information to the database.
          tweet_item.save()

     else:
          print ('Ok')



