from rest_framework.generics import CreateAPIView
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status

class Register(CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, format=None):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)