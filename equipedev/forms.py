from django import forms
from .models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ["nom", "prix"]
        labels = {
            "nom": "Nom du produit",
            "prix": "Prix (FCFA)",
        }
        widgets = {
            "nom": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ex : Ordinateur portable"
            }),
            "prix": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Ex : 150000"
            }),
        }
