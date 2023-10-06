# Importa o módulo 'render' de 'django.shortcuts'
from django.shortcuts import render


# Função para renderizar a página inicial
def index(request):
    return render(request, 'galery/index.html')


# Função para renderizar a página de imagem
def image(request):
    return render(request, 'galery/image.html')
