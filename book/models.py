from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    GENRE_CHOICE=[
        ('fiction','Fiction'),
        ('non-fiction','Non-Fiction'),
        ('science','Science'),
        ('technology','Technology'),
        ('history','History'),
        ('other','Other'),
    ]
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50, choices=GENRE_CHOICE)
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    average_rating=models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0),MaxValueValidator(5)],
        default=0
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-detail',kwargs={'pk':self.pk})