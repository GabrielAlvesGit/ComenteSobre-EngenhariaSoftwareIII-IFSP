from django.urls import path
from .views import HomePageView, SearchPageView

urlpatterns = [
    path('', SearchPageView.as_view()),
    path('home', HomePageView.as_view()),
    path('search', SearchPageView.as_view()),
]