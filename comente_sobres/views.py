from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from unidecode import unidecode
from .models import Topico
from .models import Usuario
from .models import Comentario
from django.db.models import Q
from django.db import IntegrityError

SEARCH_TEMPLATE = 'search.html'
HOME_TEMPLATE = 'home.html'


class HomePageView(View):
    def get(self, request, topico=None, msg=None):
        """Página principal do Comente Sobre."""
        context = {'topico': topico, 'msg': msg}

        return render(request, HOME_TEMPLATE, context)


class SearchPageView(View):
    def get(self, request):
        """Página de pesquisa de tópicos do Comente Sobre."""
        return render(request, SEARCH_TEMPLATE)

    def post(self, request):
        topico = request.POST.get('topico')
        topico = unidecode(topico).lower()

        # Select
        topicos: list[Topico] = select_topicos(topico)

        # Preenchimento do contexto
        context = {'topicos': topicos, 'quantidade': len(
            topicos), 'msg': 'Encontrado'}
        if not topicos:
            context['erro'] = 'Nenhum tópico encontrado.'

        return render(request, SEARCH_TEMPLATE, context)


class CreateTopicPageView(View):
    def post(self, request):
        if request.POST.get('topico') != None and request.POST.get('nome') != None and request.POST.get('email') != None:
            msg = create_topico(request.POST)
            return redirect('home_with_param', topico=request.POST.get('topico'), msg=msg)

        return HttpResponse("Erro: Dados insuficientes para criar um tópico.", status=400)


### Funções auxiliares ###
def select_topicos(self) -> list[Topico]:
    try:
        topicos_from_db = Topico.objects.filter(Q(name__icontains=self))[:50]
        topicos_from_db = sorted(topicos_from_db, key=lambda t: unidecode(t.name.lower()))
    except Topico.DoesNotExist:
        topicos_from_db = None

    return topicos_from_db


def create_topico(self) -> str:
    usuario, _ = Usuario.objects.get_or_create(
        name=self['nome'],
        email=self['email']
    )

    _, created = Topico.objects.get_or_create(
        name=self['topico'],
        usuario_added=usuario
    )

    if not created:
        return 'Retornando tópico ja criado, pelo o usuário'
    else:
        return 'Criado com sucesso'