from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from unidecode import unidecode
from .models import Topico
from .models import Usuario
from .models import Comentario
from django.db.models import Q
from django.http import JsonResponse

SEARCH_TEMPLATE = 'search.html'
HOME_TEMPLATE = 'home.html'


class HomePageView(View):
    def get(self, request, topico:Topico=None):
        """Página principal do Comente Sobre."""
        
        order = request.GET.getlist('order')
        if order != []:
             order = order[0]
        else:
            order = 'recente'
        
        if topico == None:
            return render(request, HOME_TEMPLATE)
        
        comentarios = get_comentarios(topico)
        
        if order == 'recente':
            comentarios = comentarios.order_by('-date_added')
            
        if order == 'popular':
            comentarios = comentarios.order_by('-curtidas')
            
        if order == 'usuario':
            nome_usuario = request.GET.get('nameUser')
            usuarios = get_usuario_by_name(nome_usuario).order_by('name')

            comentarios = []
            for usuario in usuarios:
                comentarios_usuario = Comentario.objects.filter(id_usuario_added=usuario.id, id_topico=topico.id)
                comentarios += list(comentarios_usuario)

            # Obter comentários de outros usuários
            ids_usuarios = [usuario.id for usuario in usuarios]
            comentarios_outros = Comentario.objects.exclude(id_usuario_added__in=ids_usuarios).filter(id_topico=topico.id)

            comentarios += list(comentarios_outros)
        
        context = {'topico': topico, 'comentarios': comentarios, 'order': order}
        return render(request, HOME_TEMPLATE, context)
    
    def post(self, request):
        """Cria um comentário no Comente Sobre."""
        if request.POST.get('comentario') != None and request.POST.get('nome') != None and request.POST.get('email') != None and request.POST.get('topico') != None:
            comentario = create_comentario(request.POST)
            return redirect('home_with_param', topico=comentario.id_topico)
        
        if request.POST.get('curtida') == 'True' and request.POST.get('id_comentario') != None:
            comentario = Comentario.objects.get(id=request.POST.get('id_comentario'))
            comentario.curtidas += 1
            comentario.save()
            return redirect('home_with_param', topico=comentario.id_topico)

        return HttpResponse("Erro: Dados insuficientes para criar um comentário.", status=400)

class SearchPageView(View):
    def get(self, request):
        """Página de pesquisa de tópicos do Comente Sobre."""
        topico = request.GET.get('topico')
        
        if topico != None:
            topico = unidecode(topico).lower()

            # Select
            topicos: list[Topico] = get_topicos(topico)

            # Preenchimento do contexto
            context = {'topicos': topicos, 'quantidade': len(topicos)}
            if not topicos:
                context['erro'] = 'Nenhum tópico encontrado.'
            return render(request, SEARCH_TEMPLATE, context)
        else:
            return render(request, SEARCH_TEMPLATE)

    def post(self, request):
        """Cria um tópico no Comente Sobre."""
        if request.POST.get('topico') != None and request.POST.get('nome') != None and request.POST.get('email') != None:
            topico = create_topico(request.POST)
            return redirect('home_with_param', topico=topico)

        return HttpResponse("Erro: Dados insuficientes para criar um tópico.", status=400)    


### Funções auxiliares ###
def get_topicos(self) -> list[Topico]:
    try:
        topicos_from_db = Topico.objects.filter(name_unaccented__icontains=unidecode(self.lower()))[:50]
        topicos_from_db = sorted(topicos_from_db, key=lambda t: t.name_unaccented)
    except Topico.DoesNotExist:
        topicos_from_db = None

    return topicos_from_db

def get_comentarios(self) -> list[Comentario]:
    try:
        comentarios_from_db = Comentario.objects.filter(Q(id_topico__name__icontains=self.name)).order_by('-id')
    except Comentario.DoesNotExist:
        comentarios_from_db = None

    return comentarios_from_db

def get_usuario_by_name(self) -> list[Usuario]:
    try:
        usuario_from_db = Usuario.objects.filter(name__icontains=self)
    except Usuario.DoesNotExist:
        usuario_from_db = None

    return usuario_from_db

def create_topico(self) -> Topico:
    usuario, _ = Usuario.objects.get_or_create(
        name=self['nome'],
        email=self['email']
    )

    topico, _ = Topico.objects.get_or_create(
        name=self['topico'],
        usuario_added=usuario
    )
    return topico

def create_comentario(self) -> Comentario:
    usuario, _ = Usuario.objects.get_or_create(
        name=self['nome'],
        email=self['email']
    )

    topico = Topico.objects.get(id=self['topico'])

    comentario, _ = Comentario.objects.get_or_create(
        id_topico=topico,
        id_usuario_added_id=usuario.id,
        texto=self['comentario']
    )
    return comentario