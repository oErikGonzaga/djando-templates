# Importa o módulo 'render' de 'django.shortcuts'
from django.shortcuts import render, get_object_or_404
from galery.models import Fotografia

# Função para renderizar a página inicial


def index(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)
    return render(request, 'galery/index.html', {"cards": fotografias})


# Função para renderizar a página de imagem
def image(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    texto_descricao = fotografia.descricao
    texto_formatado = texto_descricao.replace('<br>', '\n')
    return render(request, 'galery/image.html',
                  {'fotografia': fotografia, 'texto_formatado': texto_formatado})


def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)

    return render(request, 'galery/buscar.html', {"cards":  fotografias})
