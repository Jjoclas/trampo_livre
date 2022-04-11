from rest_framework import viewsets

from .models.avaliacoes import AvaliacoesSerializer, Avaliacoes
from .models.atividades import AtividadesSerializer, Atividades
from .models.profissionais import ProfissionaisSerializer, Profissionais
from .models.setor import SetorSerializer, Setor
from .models.usuarios import UsuariosSerializer, Usuarios
from .models.agenda import AgendaSerializer, Agenda



class UsuariosViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

class ProfissionaisViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Profissionais.objects.all()
    serializer_class = ProfissionaisSerializer

class SetorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer

class AvaliacoesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacoesSerializer

class AtividadesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Atividades.objects.all()
    serializer_class = AtividadesSerializer
