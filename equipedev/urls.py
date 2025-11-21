from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("produits/", views.produit_list, name="produit_list"),          # liste + ajout
    path("produits/<int:pk>/edit/", views.produit_edit, name="produit_edit"),   # édition
    path("produits/<int:pk>/delete/", views.produit_delete, name="produit_delete"),  # suppression
]
