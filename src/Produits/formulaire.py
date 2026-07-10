from django import forms
from .models import Produits


class AjoutProduit(forms.ModelForm):
    class Meta:
        model = Produits
        fields = [
            'name',
            'category',
            'price',
            'quantite',
            'description',
            'date_expire',
            'image',
        ]