from django.shortcuts import render
from core.models import Lib
from core.serializers import LibSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def LibList(request):
  lib = Lib.objects.all()
  serializer = LibSerializer(lib, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def LibPost(request):
  serializer = LibSerializer(data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def LibPut(request, pk):
  lib = Lib.objects.get(id=pk)
  serializer = LibSerializer(lib, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def LibDelete(request,pk):
  lib = Lib.objects.get(id=pk)
  lib.delete()
  return Response('apagado')
