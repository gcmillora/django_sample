from django.shortcuts import render
from rest_framework.views import APIView
from ..serializers import RepositorySerializer
from ..models import Repository
from rest_framework.response import Response
from rest_framework import status
from ..controllers.repository import RepositoryController
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model
from utils.response_handler import ResponseHandler


class RepositoryApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def __init__(self, controller=RepositoryController()):
        self.controller = controller

    def get(self, request, *args, **kwargs):
        repositories = self.controller.get_all_repositories()
        serializer = RepositorySerializer(repositories, many=True)
        return ResponseHandler.success(serializer.data)

    def post(self, request, *args, **kwargs):
        data = {
            "title": request.data.get("title"),
            "description": request.data.get("description"),
            "url": request.data.get("url"),
            "authorNames": request.data.get("authorNames"),
        }
        serializer = RepositorySerializer(data=data)
        if serializer.is_valid():
            repository = self.controller.create_repository(data)
            serializer = RepositorySerializer(repository)
            return ResponseHandler.success(serializer.data)
        return ResponseHandler.error(serializer.errors)


class RepositoryDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def __init__(self, controller=RepositoryController()):
        self.controller = controller

    def get(self, request, name, *args, **kwargs):
        repositories = self.controller.get_repositories_by_name(name)
        serializer = RepositorySerializer(repositories, many=True)
        return ResponseHandler.success(serializer.data)
