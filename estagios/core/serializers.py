from rest_framework import serializers
from .models import Estagiario, Convenio, Estagio, Documento, Notificacao


class EstagiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estagiario
        fields = '__all__'


class ConvenioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Convenio
        fields = '__all__'


class EstagioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estagio
        fields = '__all__'


class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = '__all__'


class NotificacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacao
        fields = '__all__'
