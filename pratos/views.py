from django.http import JsonResponse

from .models import Prato


def listar_pratos(request):
    pratos = Prato.objects.values(
        "id",
        "nome",
        "preco",
        "tempo_preparo_min",
        "vegetariano",
        "categoria__nome",
    )
    return JsonResponse(list(pratos), safe=False)
