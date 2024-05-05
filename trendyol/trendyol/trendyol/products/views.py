from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, DetailView

def home_view(request):
    data = {
        "products": Product.objects.all()
    }
    return render(request, "products/home.html", data)


class HomeView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "products/home.html"

class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "products/product_detail.html"



def create_product_view(request):

    if request.method == "POST":
        product_name = request.POST.get("name")
        product_price = request.POST.get("price")
        product_made_in = request.POST.get("made_in")

        product = Product.objects.create(
            name=product_name,
            price=product_price,
            made_in=product_made_in
        )
        return redirect("/success/")

    return render(request, "products/create_product.html")


def product_create_success(request):
    return render(request, "products/product_creation_success.html")