from django.contrib import admin

# Register your models here.
from .models import SentimentEntry

admin.site.register(SentimentEntry)