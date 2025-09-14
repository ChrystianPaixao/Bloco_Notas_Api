from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('notas/', include('app_bloco_notas.urls')),
    path('notas/', include('app_usuarios.urls'))
]
