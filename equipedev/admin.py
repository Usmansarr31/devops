from django.contrib import admin
from .models import Produit

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ("id", "nom", "prix", "created_at", "updated_at")
    search_fields = ("nom",)
    list_filter = ("created_at", "updated_at")