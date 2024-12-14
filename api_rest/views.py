from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timedelta, time


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario, Lembrete
from .serializers import UsuarioSerializer, LembreteSerializer

import json


@api_view(['GET']) #vetorr de iteins
def get_usuario(request):

    if request.method == 'GET': #Verificação por padrão
        usuario = Usuario.objects.all()  #Puxa todos o s obejetos como queryset

        serializer = UsuarioSerializer(usuario, many=True) # Serializa tudo
        return Response(serializer.data) #retorna normar

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_usuario_by_id(request, pk):  
    try:
        usuario = Usuario.objects.get(usuario_id = pk) 
    except Usuario.DoesNotExist:  
        return Response(
            {"error": "Usuário não encontrado."}, 
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = UsuarioSerializer(usuario)  
    return Response(serializer.data)  


@api_view(['POST'])
def post_usuario(request):

    if request.method == 'POST':

        new_usuario = request.data

        serializer = UsuarioSerializer(data = new_usuario)

        if serializer.is_valid(): #verifica

            usuario_peso = serializer.validated_data.get('usuario_peso', 0)
            usuario_idade = serializer.validated_data.get('usuario_idade', 0)

            if 1 <= usuario_idade <=17:
                meta_dia = (usuario_peso * 40)
            elif 18 <= usuario_idade <=55:
                meta_dia = (usuario_peso * 35)
            elif 56 <= usuario_peso <=65:
                meta_dia = (usuario_peso * 30)
            elif 66 <= usuario_peso:
                meta_dia = (usuario_peso *25)

            Usuario.objects.create(
            meta_dia=meta_dia,
            **serializer.validated_data
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED) #resposta
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def put_usuario(request, pk):
    if request.method == 'PUT':

        usuario = Usuario.objects.get(usuario_id = pk)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
    
@api_view(['DELETE'])
def delete_usuario(request, pk):
    if request.method == 'DELETE':

        try:
            usuario_to_delete = Usuario.objects.get(usuario_id = pk)
            usuario_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    #--- LEMBRETE ---
    
@api_view(['GET'])
def get_lembrete(request):
    if request.method == 'GET':
        lembrete = Lembrete.objects.all()
        serializer = LembreteSerializer(lembrete, many=True)


        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_lembrete_by_id(request, pk):  
    try:
        lembrete = Lembrete.objects.get(lembrete_id = pk) 
    except Lembrete.DoesNotExist:  
        return Response(
            {"error": "Usuário não encontrado."}, 
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = LembreteSerializer(lembrete)  
    return Response(serializer.data)  

@api_view(['POST'])
def post_lembrete(request):

    if request.method == 'POST':

        new_lembrete = request.data

        serializer = LembreteSerializer(data = new_lembrete)

        if serializer.is_valid(): 
            serializer.save()      
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PUT'])
def put_lembrete(request, pk):
    if request.method == 'PUT':
        lembrete = Lembrete.objects.get(lembrete_id = pk)
        serializer = LembreteSerializer(lembrete, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['DELETE'])
def delete_lembrete(request, pk):
    if request.method == 'DELETE':
        
        try:
            lembrete_to_delete = Lembrete.objects.get(lembrete_id = pk)
            lembrete_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def criar_lembretes(request):

    usuario_id = request.data.get('usuario_id')

    try:
        usuario = Usuario.objects.get(pk=usuario_id)  # Busca o usuário pela ID
    except Usuario.DoesNotExist:
        return Response({"error": "Usuário não encontrado."}, status=status.HTTP_404_NOT_FOUND)

    hora_atual = datetime.now()
    lembrete_dia = datetime.now().date() 
    lembretes = []
    lembrete_quantidade_agua = usuario.meta_dia/10
    hora_anterior = hora_atual
    quantidade_garrafa = 600        

    for i in range(10):
        
        simulacao_hora = hora_atual + timedelta(hours=2 * i)
        lembrete_hora = simulacao_hora.time()  
        simulacao_datetime = datetime.combine(lembrete_dia, simulacao_hora.time())
        print("Simulação como datetime:", simulacao_datetime)
        print(lembrete_hora)

        if simulacao_datetime < hora_anterior:
            lembrete_dia = (lembrete_dia + timedelta(days=1))  

        if quantidade_garrafa < lembrete_quantidade_agua:
            lembrete_mensagem = ('Hora de beber água e encher a garrafa!')
            quantidade_garrafa = 600
        else: 
            lembrete_mensagem = ('Hora de beber água')

        quantidade_garrafa = quantidade_garrafa - lembrete_quantidade_agua
        lembrete = Lembrete(usuario_id=usuario,lembrete_dia=lembrete_dia, lembrete_hora=lembrete_hora, 
                            lembrete_quantidade_agua=lembrete_quantidade_agua, lembrete_mensagem=lembrete_mensagem)
        lembrete.save()
        lembretes.append(lembrete)

    serializer = LembreteSerializer(lembretes, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
