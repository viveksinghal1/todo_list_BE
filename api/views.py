from django.db.models import manager
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import TaskSerializer
from .models import Task

# Create your views here.
@api_view(['GET'])
def apiOverview(request):

    api_urls = {
        'List': '/tasks/',
        'Details View': '/tasks/<str:pk>/',
        'Create': '/tasks/',
        'Update': '/tasks/<str:pk>/',
        'Delete': '/tasks/<str:pk>/',
    }

    return Response(api_urls)

@api_view(['GET', 'POST'])
def allTasks(request):

    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def specificTask(request, pk):

    if request.method == 'GET':
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task = Task.objects.get(id=pk)
        task.delete()

        return Response({'data': "Task deleted successfully"}, status=status.HTTP_200_OK)
