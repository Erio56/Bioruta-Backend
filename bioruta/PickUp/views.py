from django.shortcuts import render
from rest_framework.views import APIView
from PickUp.serializers import PickUpSerializer 
from rest_framework.response import Response
from rest_framework import permissions, status

from Users.serializers import UserSerializer

from Users.models import UserAccount


class PickUpRequest(APIView):
   def post(self, request):
      data = request.data
      
      pickUp = PickUpSerializer(data=data)
         
      if not pickUp.is_valid():
         return Response({'Error':'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
         
      user = request.user
      user = UserSerializer(user).data
      
      user = UserAccount.objects.get(email=user['email'])
      pickUp.create(pickUp.validated_data,user=user)
      
      return Response({'Success':'Registered successfuly'}, status=status.HTTP_200_OK)
      

