from rest_framework import serializers

from PickUp.models import PickUp, Material
from Users.models import UserAccount, UserAddress
from Users.serializers import UserSerializer
from django.contrib.auth import get_user_model



class MaterialSerializer(serializers.ModelSerializer):
   class Meta:
      model = Material
      fields = ['materialType', 'height', 'width', 'weight']


class PickUpSerializer(serializers.ModelSerializer):
   materials = MaterialSerializer(many=True)
   address = UserAddress()
   
   class Meta:
      model = PickUp
      fields = ['address', 'state', 'timeToPickUp', 'requestedDate', 'materials']
      
   def create(self, validated_data, user):
      model = get_user_model()
      materials_data = validated_data.pop('materials')
      pickUp = PickUp.objects.create(**validated_data, requestedFrom=user)
      for material_data in materials_data:
         Material.objects.create(pickingUpFrom=pickUp, **material_data)
      return pickUp
   
