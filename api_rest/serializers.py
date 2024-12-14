from rest_framework import serializers

from .models import Usuario, Lembrete



class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['usuario_id', 'usuario_nome', 'usuario_peso', 'usuario_idade']

class LembreteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lembrete
        fields = ('__all__')