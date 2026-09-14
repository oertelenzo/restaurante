"""
URL configuration for config project.
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # Rotas da API sob o prefixo api/
    path("api/", include("pratos.urls")),
]
