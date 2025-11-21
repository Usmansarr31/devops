from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit
from .forms import ProduitForm

def produit_list(request):
    # Création (formulaire d’ajout)
    if request.method == "POST":
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("produit_list")
    else:
        form = ProduitForm()

    produits = Produit.objects.order_by("-created_at")
    context = {
        "form": form,
        "produits": produits,
    }
    return render(request, "equipedev/list_produit.html", context)


def produit_edit(request, pk):
    produit = get_object_or_404(Produit, pk=pk)

    if request.method == "POST":
        form = ProduitForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect("produit_list")
    else:
        form = ProduitForm(instance=produit)

    context = {
        "form": form,
        "produit": produit,
    }
    return render(request, "equipedev/edit_produit.html", context)


def produit_delete(request, pk):
    produit = get_object_or_404(Produit, pk=pk)

    if request.method == "POST":
        produit.delete()
        return redirect("produit_list")

    # simple confirmation
    return render(request, "equipedev/confirm_delete.html", {"produit": produit})
