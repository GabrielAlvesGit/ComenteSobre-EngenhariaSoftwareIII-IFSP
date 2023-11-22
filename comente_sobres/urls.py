from django.urls import path
from .views import HomePageView, SearchPageView, CreateTopicPageView

urlpatterns = [
    path('', SearchPageView.as_view(), name='search'),
    path('home', HomePageView.as_view(), name='home_without_param'),
    path('home/<str:topico>/<str:msg>/', HomePageView.as_view(), name='home_with_param'),
    path('search', SearchPageView.as_view(), name='search'),
    path('create-topic', CreateTopicPageView.as_view(), name='create-topic'),
]