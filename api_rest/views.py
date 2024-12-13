from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Usuario
from .serializers import UsuarioSerializer

import json


@api_view(['GET']) #vetorr de iteins
def get_usuario(request):

    if request.method == 'GET': #Verificação por padrão
        usuario = Usuario.objects.all()  #Puxa todos o s obejetos como queryset

        serializer = UsuarioSerializer(usuario, many=True) # Serializa tudo
        return Response(serializer.data) #retorna normar

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post_usuario(request):

    if request.method == 'POST':

        new_usuario = request.data

        serializer = UsuarioSerializer(data = new_usuario)

        if serializer.is_valid(): #verifica
            serializer.save()      #salva
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