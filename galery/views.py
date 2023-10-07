# Importa o módulo 'render' de 'django.shortcuts'
from django.shortcuts import render
from galery.models import Fotografia

# Função para renderizar a página inicial


def index(request):
    fotografias = Fotografia.objects.all()
    return render(request, 'galery/index.html', {"cards": fotografias})


# Função para renderizar a página de imagem
def image(request):
    return render(request, 'galery/image.html')
