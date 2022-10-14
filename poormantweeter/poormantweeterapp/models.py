from django.db import models

# Create Tweet models.
class Tweet(models.Model):
     author = models.CharField(max_length=200)
     body = models.TextField(max_length=50)
     date = models.DateTimeField(auto_now_add=True)

     def __str__(self):
          return self.author
