from django.db import models
from pydantic import (BaseModel,StrictBool,StrictInt,StrictStr,)
#Historia 1 - Permisos y modulos
class Module (models.Model):
    name = models.CharField(max_length=40,blank=False,default="N/D")
    description = models.CharField(max_length=40,blank=True)

class Role (models.Model):
    name = models.CharField(max_length=40,blank=False,default="N/D")
    description = models.CharField(max_length=40,blank=True)
    
class Permissions (models.Model):
    role = models.ForeignKey(Role,on_delete=models.CASCADE)
    module = models.ForeignKey(Module,on_delete=models.CASCADE)
    create = models.BooleanField(null=False,default=False)
    read = models.BooleanField(null=False,default=False)
    update = models.BooleanField(null=False,default=False)
    delete = models.BooleanField(null=False,default=False)

#Historia 2 - Usuarios
class Address(models.Model):
    department = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    suburb = models.CharField(max_length=40)
    street = models.CharField(max_length=40)
    residence = models.CharField(max_length=40)
    reference = models.CharField(max_length=250)

class ProfileType(models.Model):
    profileName = models.CharField(max_length=40)
    description = models.CharField(max_length=100)

class User(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    profileType = models.ForeignKey(ProfileType, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL,null=True)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=50)
    dni = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    principalCellphone = models.CharField(max_length=10)
    auxiliarCellphone = models.CharField(max_length=10)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)

class PetCategory(models.Model):
    name = models.CharField(max_length=50)
    

class Pet(models.Model):
    name = models.CharField(max_length=70)
    category = models.ForeignKey(PetCategory, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    birthDate = models.DateField()
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    isSterilized = models.BooleanField(null=False,default=False)
    isAdopted = models.BooleanField(null=False,default=False)
    vaccines = models.ManyToManyField(Vaccine)
    



