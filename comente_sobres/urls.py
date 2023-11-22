from django.urls import path
from .views import HomePageView, SearchPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('home', HomePageView.as_view(), name='home_without_param'),
    path('home/<str:topico>/', HomePageView.as_view(), name='home_with_param'),
    path('search', SearchPageView.as_view(), name='search'),
]