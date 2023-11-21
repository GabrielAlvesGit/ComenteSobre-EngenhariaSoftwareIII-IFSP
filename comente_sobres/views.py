from django.shortcuts import render
from django.views import View
from unidecode import unidecode
from .models import Topico
from django.db.models import Q

class HomePageView(View):
    def get(self, request):
        """Página principal do Comente Sobre."""
        return render(request, 'home.html')

class SearchPageView(View):
    def get(self, request):
        """Página de pesquisa de tópicos do Comente Sobre."""
        return render(request, 'search.html')

    def post(self, request):
        """Página de pesquisa de tópicos do Comente Sobre."""
        topico = request.POST.get('topico')
        topico_normalizado = unidecode(topico).lower()
        
        try:
            topicos_from_db = Topico.objects.filter(Q(name__icontains=topico_normalizado))
            for topico in topicos_from_db:
                print(topico.id)
                print(topico.name)
        except Topico.DoesNotExist:
            topicos_from_db = None
            
        return render(request, 'search.html')