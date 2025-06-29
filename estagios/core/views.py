from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count

from .models import Estagiario, Convenio, Estagio, Documento, Notificacao
from .serializers import (
    EstagiarioSerializer,
    ConvenioSerializer,
    EstagioSerializer,
    DocumentoSerializer,
    NotificacaoSerializer,
)


class EstagiarioViewSet(viewsets.ModelViewSet):
    """CRUD de estagiários"""
    queryset = Estagiario.objects.all()
    serializer_class = EstagiarioSerializer
    filterset_fields = ['status']
    search_fields = ['nome']
    ordering_fields = ['nome', 'status']


class ConvenioViewSet(viewsets.ModelViewSet):
    """CRUD de convênios"""
    queryset = Convenio.objects.all()
    serializer_class = ConvenioSerializer


class EstagioViewSet(viewsets.ModelViewSet):
    """CRUD de estágios"""
    queryset = Estagio.objects.all()
    serializer_class = EstagioSerializer


class DocumentoViewSet(viewsets.ModelViewSet):
    """Upload e download de documentos"""
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer


class NotificacaoViewSet(viewsets.ModelViewSet):
    """Gerencia notificações"""
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer

    @action(detail=True, methods=['post'])
    def marcar_lida(self, request, pk=None):
        notificacao = self.get_object()
        notificacao.lida = True
        notificacao.save()
        return Response({'status': 'notificação marcada como lida'})


class DashboardView(APIView):
    """Retorna dados resumidos do sistema"""
    def get(self, request):
        total_estagiarios = Estagiario.objects.count()
        estagios_ativos = Estagio.objects.filter(status='Em andamento').count()
        convenios_ativos = Convenio.objects.count()
        documentos_enviados = Documento.objects.count()
        data = {
            'total_estagiarios': total_estagiarios,
            'estagios_ativos': estagios_ativos,
            'convenios_ativos': convenios_ativos,
            'documentos_enviados': documentos_enviados,
        }
        return Response(data)
