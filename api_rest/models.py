from django.db import models

# Create your models here.

class Usuario(models.Model):
    
    usuario_id = models.AutoField(primary_key=True)
    usuario_nome = models.CharField(max_length=20, default='')
    usuario_peso = models.IntegerField(default=0)
    usuario_idade = models.IntegerField(default=0)
    meta_dia = models.IntegerField(default=0)

    def __str__(self):
        return f'Nome: {self.usuario_nome} | Idade: {self.usuario_idade} | Peso: {self.usuario_peso}'
    
class Lembrete(models.Model):
    lembrete_id = models.AutoField(primary_key=True)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=0)
    lembrete_dia = models.DateField()
    lembrete_hora = models.TimeField()
    lembrete_quantidade_agua = models.IntegerField()