# Importa o módulo 'render' de 'django.shortcuts'
from django.shortcuts import render, get_object_or_404
from galery.models import Fotografia

# Função para renderizar a página inicial


def index(request):
    fotografias = Fotografia.objects.all()
    return render(request, 'galery/index.html', {"cards": fotografias})


# Função para renderizar a página de imagem
def image(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galery/image.html', {'fotografia': fotografia})
