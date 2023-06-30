from django.db import models
from Users.models import UserAccount

# Create your models here.

class StoreItem(models.Model):
   itemName = models.CharField(max_length=50)
   price = models.IntegerField()
   status = models.CharField(max_length=50)

class Buyer(models.Model):
   user = models.ForeignKey(UserAccount, related_name='fk_buyers', on_delete=models.CASCADE)
   buyedOn = models.DateTimeField(auto_now=True)
