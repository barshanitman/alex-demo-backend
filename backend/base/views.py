from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Project

# Create your views here.
@api_view(["GET","POST"])
def get_projects(request):

    if request.method == "GET":
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects,many=True)
        try:
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_503_SERVICE_UNAVAILABLE)



    elif request.method == "POST":
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    return Response("Endpoint only accepts GET and POST",status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    




@api_view(["POST"])
def add_project(request):
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



    










    

