from django.urls import path, register_converter
from comente_sobres.models import Topico
from .views import HomePageView, SearchPageView

class TopicoConverter:
    regex = r'[^/]+-\d+'

    def to_python(self, value):
        topico_name, topico_id = value.split('-')
        return Topico.objects.get(name=topico_name, id=topico_id)

    def to_url(self, value):
        return f"{value.name}-{value.id}"

register_converter(TopicoConverter, 'Topico')

urlpatterns = [
    path('', SearchPageView.as_view(), name='search'),
    path('home', HomePageView.as_view(), name='home_without_param'),
    path('home/<str:nome_topico>/<int:id_topico>', HomePageView.as_view(), name='home_with_param'),
    path('search', SearchPageView.as_view(), name='search'),
]