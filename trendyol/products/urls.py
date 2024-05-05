from django.urls import path
from .views import HomeView, ProductDetailView, create_product_view, product_create_success

app_name = "product"

urlpatterns = [
    path(
        "", 
        HomeView.as_view(),
        name="home"
    ),
    path(
        "product-details/<int:pk>-<slug:slug>/",
        ProductDetailView.as_view(),
        name="product-detail"
    ),
    path(
        "create-product/",
        create_product_view,
        name="create-product"
    ),
    path(
        "success/",
        product_create_success,
        name="create-success"
    )
]

