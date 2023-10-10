# Importa o módulo 'admin' de 'django.contrib' e 'include' de 'django.urls'
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# URLs do projeto
urlpatterns = [
    # Define a URL 'admin/' para o painel de administração
    path('admin/', admin.site.urls),

    # Inclui as URLs da aplicação 'galery' (definidas anteriormente)
    path('', include('galery.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
