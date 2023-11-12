from django.shortcuts import render

def index(request):
    """Página principal do Comente Sobre."""
    return render(request, 'index.html')