import json
import requests

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions

from .models import WorkSpace, Entity, Relationship, Association
from .utils import graph


class WorkSpaceView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        entity_1 = data['actor']
        entity_2 = data['related']
        relation = data['relation']
        workspace = data['workspace']

        workspace, _ = WorkSpace.objects.get_or_create(name=workspace)
        relationship, _ = Relationship.objects.get_or_create(name=relation)
        entity_1, _ = Entity.objects.get_or_create(
            name=entity_1, workspace=workspace)
        entity_2, _ = Entity.objects.get_or_create(
            name=entity_2, workspace=workspace)

        association, _ = Association.objects.get_or_create(
            entity_1=entity_1, entity_2=entity_2,
            relationship=relationship, workspace=workspace)

        graph.add_entity(entity_1)
        graph.add_entity(entity_2)
        graph.add_association(association)

        return Response({'graph': workspace.id}, status=status.HTTP_200_OK)


class Neo4jQueryView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        response = ""
        data = request.data
        query = data["query"]
        if query:
            result = graph.run(query)
            response = json.dumps(result.data())

        return Response({'content': response}, status=status.HTTP_200_OK)
