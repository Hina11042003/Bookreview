from django.shortcuts import render, redirect
from textblob import TextBlob
from .forms import SentimentForm
from .models import SentimentEntry


def home(request):
    if request.method == 'POST':
        form = SentimentForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)

            blob = TextBlob(entry.text)
            polarity = blob.sentiment.polarity

            if polarity > 0.1:
                sentiment = "Positive"
            elif polarity < -0.1:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"

            entry.polarity = round(polarity, 2)
            entry.sentiment = sentiment
            entry.save()

            return redirect('sentiment-home-result', entry_id=entry.id)
    else:
        form = SentimentForm()

    return render(request, 'sentiment_lab/home.html', {'form': form, 'result': None})


def home_with_result(request, entry_id):
    form = SentimentForm()
    result = SentimentEntry.objects.get(id=entry_id)
    return render(request, 'sentiment_lab/home.html', {'form': form, 'result': result})