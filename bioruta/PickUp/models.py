from django.db import models
from Users.models import UserAccount, UserAddress

# Create your models here.  

class PickUp(models.Model):
   requestedFrom = models.ForeignKey( UserAccount, on_delete=models.CASCADE )
   address = models.ForeignKey(UserAddress, on_delete=models.CASCADE)
   state = models.CharField(max_length=100)
   timeToPickUp = models.TimeField()
   requestedDate = models.DateField()
   
   def create(self, data, user: UserAccount):
      PickUp(address=data['address'], requestedFrom=user, state=data['state'], timeToPickUp=data['timeToPickUp'], requestedDate=data['requestedDate']).save()
      
   
class Material(models.Model):
   pickingUpFrom = models.ForeignKey( PickUp, on_delete=models.CASCADE )
   materialType = models.CharField(max_length=200)
   height = models.CharField(max_length=5)
   weight = models.CharField(max_length=5)
   width = models.CharField(max_length=5)

   