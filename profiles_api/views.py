from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from .serializers import HelloSerializer


class HelloApiView(APIView):
    serializer_class = HelloSerializer

    def get(self, request, format=None):
        cities = ['Toronto', 'Ottawa', 'Bangalore']
        return Response({'message': 'hello', 'cities': cities})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello, {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'message': 'PUT'})

    def patch(self, request, pk=None):
        return Response({'message': 'PATCH'})

    def delete(self, request, pk=None):
        return Response({'message': 'DELETE'})


class HelloViewSet(ViewSet):
    serializer_class = HelloSerializer

    def list(self, request):
        cities = ['Toronto', 'Ottawa', 'Bangalore']
        return Response({'message': 'Hello!', 'cities': cities})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello, {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})
