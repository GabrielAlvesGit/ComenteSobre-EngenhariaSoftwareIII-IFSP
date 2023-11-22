from django.shortcuts import render, redirect
from django.views import View
from unidecode import unidecode
from .models import Topico
from django.db.models import Q

SEARCH_TEMPLATE = 'search.html'

class HomePageView(View):
    def get(self, request, topico=None):
        """Página principal do Comente Sobre."""
        context = {'topico': topico}
        
        return render(request, 'home.html', context)

from django.shortcuts import render, get_object_or_404
from unidecode import unidecode

class SearchPageView(View):
    def get(self, request):
        """Página de pesquisa de tópicos do Comente Sobre."""
        return render(request, SEARCH_TEMPLATE)

    def post(self, request):
        topico = request.POST.get('topico')
        topico = unidecode(topico).lower()

        ## Select
        topicos: list[Topico] = select_topicos(topico)
        
        ## Preenchimento do contexto
        context = {'topicos': topicos, 'quantidade': len(topicos)}
        if not topicos:
            context['erro'] = 'Nenhum tópico encontrado.'

        return render(request, SEARCH_TEMPLATE, context)


## Funções auxiliares
def select_topicos(self) -> list[Topico]:
    try:
        topicos_from_db = Topico.objects.filter(Q(name__icontains=self))
    except Topico.DoesNotExist:
        topicos_from_db = None
        
    return topicos_from_db