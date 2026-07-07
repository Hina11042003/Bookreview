from django.db import models

class SentimentEntry(models.Model):
    text = models.TextField()
    polarity = models.FloatField(blank=True, null=True)
    sentiment = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]