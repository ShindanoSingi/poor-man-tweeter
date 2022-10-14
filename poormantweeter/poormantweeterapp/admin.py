from django.contrib import admin

# Register Tweet model.
from .models import Tweet

admin.site.register(Tweet)