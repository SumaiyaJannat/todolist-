from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser


from .serializers import TaskSerializer

from .models import Task
# Create your views here.



class ApiOverview(APIView):
    def get(self, request):
        api_urls = {
            'List': '/task-list/',
            'Detail View': '/task-detail/<str:pk>/',
            'Create': '/task-create/',
            'Update': '/task-update/<str:pk>/',
            'Delete': '/task-delete/<str:pk>/',
        }
        return Response(api_urls)

class TaskList(APIView):
    def get(self, request):
        tasks = Task.objects.all().order_by('-id')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class TaskDetail(APIView):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

class TaskCreate(APIView):
    def post(self, request):
        print(request.data)
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskUpdate(APIView):
    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskDelete(APIView):
    def delete(self, request, pk):
        task = Task.objects.get(id=pk)
        task.delete()
        return Response('Item successfully deleted!', status=status.HTTP_204_NO_CONTENT)





