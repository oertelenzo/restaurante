from django.urls import path

from . import views

urlpatterns = [
    path("pratos/", views.listar_pratos, name="listar_pratos"),
]
