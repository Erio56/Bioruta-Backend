from django.db import models
from PickUp.models import PickUp

# Create your models here.

class TrackingInfo(models.Model):
   PickUpOrder = models.ForeignKey(PickUp, on_delete=models.CASCADE)
   status = models.CharField(max_length=20)
   timeStamp = models.TimeField(auto_now=True)
   