from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse



# REST IMPORT 

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Snippet
from .models import Students
from .serializers import SnippetSerializer


# REST IMPORTS 
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status


@api_view(['GET','POST','PUT'])
def snippet_list(request):
    if request.method =='GET':
        snippet_obj = Snippet.objects.all()
        serializer = SnippetSerializer(snippet_obj,many=True)
        context = {'message':'This is a GET request','data':serializer.data}
        return Response(context)
    
    elif request.method == 'PUT':
        snippet_obj = Snippet.objects.all()
        serializer = SnippetSerializer(snippet_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method =='POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'This is a GET request','response_code':200})
        
@api_view(['GET','DELETE','PUT','PATCH'])
def snippet_obj(request,pk):
    if request.method=='GET':
        try:
          snippet_obj=Snippet.objects.get(id=pk)
          serializer = SnippetSerializer(snippet_obj)
          context = {'message':'This is a GET request','data':serializer.data}
          return Response(context)
        except Snippet.DoesNotExist:
            return Response({'message':'data not found ','response_code':404})
        
    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = SnippetSerializer(snippet_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method=='DELETE':
        try:
          snippet_obj=Snippet.objects.get(id=pk)
          snippet_obj.delete()
          return Response({'message':'Snippet deleted'})
        except Snippet.DoesNotExist:
            return Response({'message':'Data already deleted ','response_code':404})