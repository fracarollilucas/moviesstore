from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="cart.index"),
    path("<int:id>/add/", views.add_to_cart, name="cart.add_to_cart"),
    path("clear/", views.clear, name="cart.clear"),
    path("purchase/", views.purchase, name="cart.purchase"),
    path("orders", views.orders, name="accounts.orders"),
]
