from django.urls import path

from .views import *
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('',Affichage.as_view(), name="vue-home"),
    # path('ajout/',Ajout_produit,name='ajout')
    path('ajout/',AjoutProduits.as_view(),name='ajout')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)