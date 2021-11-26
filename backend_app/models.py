from django.db import models
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
class ProfileType(models.Model):
    name = models.CharField(max_length=40,blank=False,null=False,default="N/D")
    description = models.CharField(max_length=100,blank=False,null=False,default="N/D")



class Address(models.Model):
    department = models.CharField(max_length=40,blank=False,null=False,default="N/D")
    city = models.CharField(max_length=40,blank=False,null=False,default="N/D")
    suburb = models.CharField(max_length=40,blank=False,null=False,default="N/D")
    street = models.CharField(max_length=40,blank=False,null=False,default="N/D")
    residence = models.CharField(max_length=40,blank=False,null=False,default="N/D")
    reference = models.CharField(max_length=250,blank=False,null=False,default="N/D")

class User(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    profileType = models.ForeignKey(ProfileType, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.SET_NULL,null=True)
    email = models.CharField(max_length=40,blank=False,null=False,default="N/D")
    password = models.CharField(max_length=40,blank=False,null=False,default="N/D")
    firstName = models.CharField(max_length=40,blank=False,null=False,default="N/D")
    lastName = models.CharField(max_length=50,blank=False,null=False,default="N/D")
    dni = models.CharField(max_length=30,blank=False,null=False,default="N/D")
    age = models.CharField(max_length=3,blank=False,null=False,default="N/D")
    principalCellphone = models.CharField(max_length=10,blank=False,null=False,default="N/D")
    auxiliarCellphone = models.CharField(max_length=10,blank=False,null=False,default="N/D")
    motto = models.CharField(max_length=300, blank=False,null=False,default="N/D")
    biography = models.CharField(max_length=1000,blank=False,null=False,default="N/D")
    verified = models.BooleanField(null=False,default=False)
    active = models.BooleanField(null=False,default=True)
    secureQuestion = models.CharField(max_length=300,blank=False,null=False,default="N/D")
    secureAnswer = models.CharField(max_length=100,blank=False,null=False,default="N/D")
    token = models.CharField(max_length=2024,blank=False,null=False,default="N/D")


class Vaccine(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False,default="N/D")

class PetCategory(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False,default="N/D")
    
class Breed(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False,default="N/D")

class Pet(models.Model):
    name = models.CharField(max_length=70,blank=False,null=False,default="N/D")
    category = models.ForeignKey(PetCategory, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    birthDate = models.DateField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    color = models.CharField(max_length=50,blank=False,null=False,default="N/D")
    size = models.CharField(max_length=10,blank=False,null=False,default="N/D")
    gender = models.CharField(max_length=10,blank=False,null=False,default="N/D")
    isSterilized = models.BooleanField(null=False,default=False)
    isAdopted = models.BooleanField(null=False,default=False) 
    vaccines = models.ManyToManyField(Vaccine)
    showDetails = models.BooleanField(null=False,default=False)
    description = models.CharField(max_length=1000,blank=False,null=False,default="N/D")


class AdoptionRequest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    accepted = models.BooleanField(null=False,default=False)


