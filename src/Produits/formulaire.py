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

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Nom du produit'
            }),

            'category': forms.Select(attrs={
                'class': 'input'
            }),

            'price': forms.NumberInput(attrs={
                'class': 'input'
            }),

            'quantite': forms.NumberInput(attrs={
                'placeholder': 'La quantité du produit',
                'class': 'input'
            }),

            'description': forms.Textarea(attrs={
                'placeholder': 'Description',
                'class': 'textarea'
            }),

            'date_expire': forms.DateInput(attrs={
                'class': 'input',
                'type': 'date'
            }),

            'image': forms.ClearableFileInput(attrs={
                'class': 'input-file'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].error_messages = {
            'required': 'Le nom est obligatoire.',
        }

        self.fields['category'].error_messages = {
            'required': 'La catégorie est obligatoire.',
        }

        self.fields['price'].error_messages = {
            'required': 'Le prix est obligatoire.',
            'invalid': 'Veuillez saisir un prix valide.',
        }

        self.fields['quantite'].error_messages = {
            'required': 'La quantité est obligatoire.',
            'invalid': 'Veuillez saisir une quantité valide.',
        }

        self.fields['description'].error_messages = {
            'required': 'La description est obligatoire.',
        }

        self.fields['date_expire'].error_messages = {
            'required': "La date d'expiration est obligatoire.",
            'invalid': "La date n'est pas valide.",
        }

        self.fields['image'].error_messages = {
            'required': "L'image est obligatoire.",
        }