# Importa o módulo 'render' de 'django.shortcuts'
from django.shortcuts import render


# Função para renderizar a página inicial

def index(request):
    dados = {
        1: {"nome": "Nebulosa de Carina",
            "legenda": "webbtelescope.org / NASA / James Webb"},
        2: {"nome": "Galáxia NGC 1079",
            "legenda": "nasa.org / NASA / Hubble"}
    }

    return render(request, 'galery/index.html', {"cards": dados})


# Função para renderizar a página de imagem
def image(request):
    return render(request, 'galery/image.html')
