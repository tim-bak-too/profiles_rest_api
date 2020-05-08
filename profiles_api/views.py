from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    def get(self, request, format=None):
        cities = ['Toronto', 'Ottawa', 'Bangalore']
        return Response({'message': 'hello', 'cities': cities})
    
