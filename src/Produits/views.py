from django.shortcuts import render

from .models import *
# Create your views here.

def home (request):
    donnes = Produits.objects.all
    context = {
        "donnes":donnes
    }
    return render(request,'Produits/home.html',context)