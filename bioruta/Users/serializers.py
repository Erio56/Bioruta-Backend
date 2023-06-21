from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core import exceptions
from rest_framework.serializers import as_serializer_error

from django.contrib.auth.password_validation import validate_password

#User = get_user_model()

class UserCreateSerializer(serializers.ModelSerializer):
   class Meta:
      model = get_user_model()
      fields = ('first_name','last_name', 'email', 'password')
      
   def create(self, validated_data):
      User = get_user_model()
      user = User.objects.create_user(
         first_name=validated_data['first_name'],
         last_name=validated_data['last_name'],
         email=validated_data['email'],
         password=validated_data['password'],
      )
      return user
   
   def validate(self, data):
      try:
         validate_password(password=data.get('password'))
      except exceptions.ValidationError as e:
         serializer_errors = as_serializer_error(e)
         raise exceptions.ValidationError(
            {
               'password1': serializer_errors['non_field_errors'],
               'password2': serializer_errors['non_field_errors']
            }
         )
      return data
   
class UserSerializer(serializers.ModelSerializer):
   class Meta:
      model = get_user_model()
      fields = ('first_name','last_name', 'email')