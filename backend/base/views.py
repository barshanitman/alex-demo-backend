from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import ProjectSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Project,User


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
    
   
@api_view(["GET"])
def get_project_by_id(request,id):
    project = Project.objects.get(id=int(id))
    if project is not None:
         serializer = ProjectSerializer(project)
         return Response( serializer.data,status=status.HTTP_200_OK) 
    return Response("Project does not exist",status=status.HTTP_204_NO_CONTENT)

@api_view(["GET"])
def get_all_users(request):
    users = User.objects.all()
    if users is not None:
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)
    
    return Response("No users",status=status.HTTP_204_NO_CONTENT)


        
    

    

