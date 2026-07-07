from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sentiment-home'),
    path('result/<int:entry_id>/', views.home_with_result, name='sentiment-home-result'),
]