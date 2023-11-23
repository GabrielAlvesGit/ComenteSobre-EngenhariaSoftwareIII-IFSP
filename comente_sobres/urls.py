from django.urls import path, register_converter
from comente_sobres.models import Topico
from .views import HomePageView, SearchPageView

class TopicoConverter:
    regex = '[^/]+'

    def to_python(self, value):
        return Topico.objects.get(name=value)

    def to_url(self, value):
        return str(value.name)

register_converter(TopicoConverter, 'Topico')

urlpatterns = [
    path('', SearchPageView.as_view(), name='search'),
    path('home', HomePageView.as_view(), name='home_without_param'),
    path('home/<Topico:topico>/', HomePageView.as_view(), name='home_with_param'),
    path('search', SearchPageView.as_view(), name='search'),
]