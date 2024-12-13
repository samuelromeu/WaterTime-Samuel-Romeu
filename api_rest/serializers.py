from rest_framework import serializers

from .models import Usuario, Lembrete



class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')

class LembreteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lembrete
        fields = ('__all__')