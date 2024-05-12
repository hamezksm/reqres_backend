from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer, UserLoginSerializer

# Create your views here.

class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

class UserLoginViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if(serializer.is_valid):
            username = serializer.validate_data['username']
            email = serializer.validate_data['email']
            password = serializer.validate_data['password']

            if username is not None:
                user = authenticate(username=username, password=password)
            else: 
                user = authenticate(email=email, password=password)

            if user:
                return Response({'message': 'Login successful', 'user_id': user.id}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Unable to log in with provided credentials'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)