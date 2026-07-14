from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView

from .models import *

from django.contrib import messages
from datetime import datetime
from .formulaire import AjoutProduit
from django.urls import reverse_lazy
# Create your views here.

# def home (request):
#     donnes = Produits.objects.all
#     context = {
#         "donnes":donnes
#     }
#     return render(request,'Produits/home.html',context)



class Affichage(ListView):
    template_name = 'Produits/home.html'
    queryset = Produits.objects.all()    


class AjoutProduits(CreateView):

    model = Produits
    form_class = AjoutProduit
    template_name = 'Produits/ajout.html'
    success_url = reverse_lazy('vue-home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# def Ajout_produit(request):
#     errors = {}

#     Category = Categories.objects.all()

#     if request.method == 'POST':

#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         quantite = request.POST.get('quantite')
#         description = request.POST.get('description')
#         date_expire_str = request.POST.get('date_expire')
#         image = request.FILES.get('image')


#         # Validation du prix
#         try:
#             price = float(price)

#             if price < 0:
#                 errors['price'] = "Le prix ne peut pas être négatif."

#         except (ValueError, TypeError):
#             errors['price'] = "Entrez un prix valide."


#         # Validation de la date
#         try:
#             date_expire = datetime.strptime(
#                 date_expire_str,
#                 '%Y-%m-%d'
#             ).date()

#         except (ValueError, TypeError):
#             errors['date_expire'] = "La date est invalide."


#         # Validation catégorie
#         try:
#             category = Categories.objects.get(
#                 pk=request.POST.get('category')
#             )

#         except Categories.DoesNotExist:
#             errors['category'] = "La catégorie est introuvable."


#         # Enregistrement si aucune erreur
#         if not errors:

#             produit = Produits(
#                 name=name,
#                 category=category,
#                 description=description,
#                 price=price,
#                 quantite=quantite,
#                 date_expire=date_expire,
#                 image=image
#             )

#             produit.save()

#             messages.success(
#                 request,
#                 "Le produit a été enregistré avec succès."
#             )

#             return redirect('vue-home')


#     return render(
#         request,
#         'Produits/ajout_produit.html',
#         {
#             "Category": Category,
#             "errors": errors
#         }
#     )

