from rest_framework.viewsets import ModelViewSet
from .serializers import JsonPlaceholderSerializer
from frameworkapi.models import JsonPlaceholder
from rest_framework.permissions import IsAuthenticated

class JsonPlaceholderViewset(ModelViewSet):
    """ Classe Viewset responsavel pela exibiçao da api na url"""
    # Autenticacao de permissao de acesso aos dados
    permission_classes = (IsAuthenticated,)

    # Complementos da viewset
    queryset = JsonPlaceholder.objects.all()
    serializer_class = JsonPlaceholderSerializer
