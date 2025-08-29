from django.urls import path, include


urlpatterns = [
    path('notas/', include('app_bloco_notas.urls'))
]
