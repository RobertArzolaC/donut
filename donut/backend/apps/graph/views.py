from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions

from .models import WorkSpace


class WorkSpaceView(APIView):
    authentication_classes = [ authentication.TokenAuthentication ]
    permission_classes = [ permissions.IsAuthenticated ]

    def post(self, request):
        data = request.data
        graph = WorkSpace.make_graph(data['data'])

        return Response({'graph': graph.id}, status=status.HTTP_200_OK)
