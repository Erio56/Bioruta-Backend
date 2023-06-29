from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import AddressSerializer

from .models import UserAddress


User = get_user_model()

from .serializers import UserCreateSerializer, UserSerializer


class RegisterView(APIView):
   permission_classes = [permissions.AllowAny]
   def post(self, request):
      data = request.data
      # first_name = data['first_name']
      # last_name = data['last_name']
      # email = data['email']
      password1 = data['password']
      password2 = data['password2']
      
      if password1 != password2:
         return Response({ 'error': 'Passwords do not coincide.' } ,status=status.HTTP_400_BAD_REQUEST)
      
      serializer = UserCreateSerializer(data=data)
      
      if not serializer.is_valid():
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      user = serializer.create(serializer.validated_data)
      user = UserSerializer(user)
      
      return Response(user.data, status=status.HTTP_201_CREATED)
      
class RetriveUserView(APIView):
   permission_classes = [permissions.IsAuthenticated]
   def get(self, request):
      
      user = request.user
      user = UserSerializer(user)
      
      return Response(user.data, status=status.HTTP_200_OK)

class RetrieveAdressView(APIView):
   permission_classes = [permissions.IsAuthenticated]
   
   def get(self, request):
      
      user = request.user
      address = AddressSerializer(UserAddress.objects.filter(user=user), many=True).data
      
      return Response(address, status=status.HTTP_200_OK)
      
   
