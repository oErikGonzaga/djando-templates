# Importa o módulo 'path' de 'django.urls'
from django.urls import path

# Importa as funções 'index' e 'image' do módulo 'views' em 'galery'
from galery.views import index, image, buscar

# URLs da aplicação 'galery'
urlpatterns = [
    # Define a URL raiz ('/') para a função 'index' e nomeia-a como 'index'
    path('', index, name='index'),

    # Define a URL 'image/' para a função 'image' e nomeia-a como 'image'
    path('image/<int:foto_id>', image, name='image'),

    path("buscar", buscar, name="buscar")
]
