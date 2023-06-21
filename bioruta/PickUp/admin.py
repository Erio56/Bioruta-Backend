from django.contrib import admin


from PickUp.models import Material, PickUp

# Register your models here.

admin.site.register(PickUp)
admin.site.register(Material)