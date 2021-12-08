import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from backend_app.models import *

class AddressNode(DjangoObjectType):
    class Meta:
        model=Address

class ModuleNode(DjangoObjectType):
    
    class Meta:
        model = Module

class RoleNode(DjangoObjectType):
    
    class Meta:
        model = Role

class ProfileTypeNode(DjangoObjectType):

    class Meta:
        model = ProfileType

class PermissionsNode(DjangoObjectType):
    class Meta:
        model = Permissions
        interface = (relay.Node,)
        fields = ('role','module','create','read','update','delete')

class UserNode(DjangoObjectType):
    class Meta:
        model = User
        interface = (relay.Node,)

class PetCategoryNode(DjangoObjectType):
    class Meta:
        model = PetCategory

class VaccineNode(DjangoObjectType):
    class Meta:
        model=Vaccine

class PetNode(DjangoObjectType):
    class Meta:
        model = Pet

class AdoptionRequestNode(DjangoObjectType):
    class Meta:
        model = AdoptionRequest
        interface = (relay.Node,)

class BreedNode(DjangoObjectType):
    class Meta:
        model = Breed

class RequestNode(DjangoObjectType):
    class Meta:
        model = AdoptionRequest



"""
    La clase "Query" definida es la que realizara todo tipo de consultas por cada
    atributo creado se creara un "resolve" que es un metodo que definira la consulta

"""
class Query(graphene.ObjectType):
    #Querys para obtener todos los objetos sin condiciones
    all_roles = graphene.List(RoleNode)
    all_modules = graphene.List(ModuleNode)
    all_profile_types = graphene.List(ProfileTypeNode)
    all_users = graphene.List(UserNode)
    all_pets = graphene.List(PetNode,idLoguer=graphene.Int())
    all_pet_categories = graphene.List(PetCategoryNode)
    all_vaccines = graphene.List(VaccineNode)
    all_breeds = graphene.List(BreedNode)
    #Querys ligadas a valores
    
    permissions  = graphene.List(PermissionsNode,roleId=graphene.Int())
    user = graphene.Field(UserNode,id=graphene.Int(),
                        firstName=graphene.String(),
                        lastName=graphene.String(),
                        email=graphene.String(),
                        dni=graphene.String(),
                        cellphone=graphene.String())
    get_users = graphene.List(UserNode,
                            firstName=graphene.String(),
                            lastName=graphene.String()
                            )
    pet = graphene.Field(PetNode,id=graphene.Int(),name=graphene.String())
    owner_pets = graphene.List(PetNode,
                            ownerId=graphene.Int(),
                            FirstName=graphene.String(),
                            LastName=graphene.String()
                            )
    request = graphene.Field(AdoptionRequestNode,senderId=graphene.Int(),petId=graphene.Int())
    favorite_owner_pets = graphene.List(
        PetNode,id=graphene.Int()
    )

    get_pets = graphene.List(PetNode,
                            categoryId = graphene.Int(),
                            categoryName=graphene.String(),
                            birthDate=graphene.Date(),
                            breed=graphene.String(),
                            color=graphene.String(),
                            size=graphene.String(),)


    all_user_request = graphene.List(RequestNode,senderId=graphene.Int(),receiverId=graphene.Int(),state=graphene.Int())
    all_request = graphene.List(RequestNode)
    
    #ALL REGISTERS
    def resolve_all_roles(self,info,**kwargs):
        return Role.objects.all()

    def resolve_all_modules(self,info,**kwargs):
        return Module.objects.all()
    
    def resolve_all_profile_types(self,info,**kwargs):
        return ProfileType.objects.all()

    def resolve_all_users(self,info,**kwargs):
        return User.objects.all()

    def resolve_all_pets(self,info,**kwargs):
        id = kwargs.get('idLoguer')
        if id is None:
            return Pet.objects.all()
        return Pet.objects.exclude(owner_id=id)

    def resolve_all_pet_categories(self,info,**kwargs):
        return PetCategory.objects.all()

    def resolve_all_vaccines(self,info,**kwargs):
        return Vaccine.objects.all()

    def resolve_all_breeds(self,info,**kwargs):
        return Breed.objects.all()

    #ESPECIFIC REGISTERS    
    def resolve_permissions(self,info,**kwargs):
        idRole = kwargs.get('roleId')
        if idRole is not None:
            return Permissions.objects.filter(role_id=idRole)

    def resolve_user(self,info,**kwargs):
        idUser = kwargs.get('id')
        firstName = kwargs.get('firstName')
        lastName = kwargs.get('lastName')
        email=kwargs.get('email')
        dni=kwargs.get('dni')
        cellphone=kwargs.get('cellphone')
        if idUser is not None:
            try:
                return User.objects.get(pk=idUser)
            except:
                return None
        elif firstName is not None:
            return User.objects.get(firstName=firstName)
        elif lastName is not None:
            return User.objects.get(lastName=lastName)
        elif email is not None:
            return User.objects.get(email=email)
        elif dni is not None:
            return User.objects.get(dni=dni)
        elif cellphone is not None:
            return User.objects.get(principalCellphone=cellphone)

    def resolve_get_users(self,info,**kwargs):
        firstName = kwargs.get('firstName')
        lastName = kwargs.get('lastName')
        if firstName is not None and lastName is not None:
            return User.objects.filter(firstName__icontains=firstName).filter(lastName__icontains=lastName)
        elif firstName is not None:
            if firstName!='':
                return User.objects.filter(firstName__icontains=firstName)
            return User.objects.all()
        elif lastName is not None:
            return User.objects.filter(lastName__icontains=lastName)

    def resolve_pet(self,info,**kwargs):
        idPet = kwargs.get('id')
        petName = kwargs.get('name')
        try:
            if idPet is not None:
                return Pet.objects.get(pk=idPet)
            elif petName is not None:
                return Pet.objects.get(name=petName)
        except:
            return None
    
    def resolve_owner_pets(self,info,**kwargs):
        idOwner = kwargs.get('ownerId')
        ownerFirstName = kwargs.get('firstName')
        ownerFirstName = kwargs.get('firstName')
        try:
            if idOwner is not None:
                return Pet.objects.filter(owner_id=idOwner)
            elif ownerFirstName is not None:
                return Pet.objects.filter(owner_firstName__icontains=ownerFirstName)
        except:
            return None
    
    def resolve_get_pets(self,info,**kwargs):
        categoryId = kwargs.get('categoryId')
        categoryName = kwargs.get('categoryName')
        birthDate= kwargs.get('birthDate')
        breed= kwargs.get('breed')
        color= kwargs.get('color')
        size= kwargs.get('size')
        isSterilized= kwargs.get('isSterilized')
        isAdopted= kwargs.get('isAdopted')
        if categoryId is not None:
            return Pet.objects.filter(category_id=categoryId)
        elif categoryName is not None:
            return Pet.objects.filter(category_name=categoryName)
        elif birthDate is not None:
            return Pet.objects.filter(birthDate=birthDate)
        elif breed is not None:
            return Pet.objects.filter(breed=breed)    
        elif color is not None:
            return Pet.objects.filter(color=color)    
        elif size is not None:
            return Pet.objects.filter(size=size)    
        elif isSterilized is not None:
            return Pet.objects.filter(isSterilized__icontains=isSterilized)    
        elif isAdopted is not None:
            return Pet.objects.filter(isAdopted=isAdopted)

    def resolve_all_user_request(self,info,**kwargs):
        senderId = kwargs.get('senderId')
        receiverId = kwargs.get('receiverId')
        if senderId is not None:
            return AdoptionRequest.objects.filter(sender_id=senderId)
        elif receiverId is not None:
            return AdoptionRequest.objects.filter(receiver_id=receiverId,state="PENDIENTE")

    def resolve_request(self,info,**kwargs):
        senderId = kwargs.get('senderId')
        petId= kwargs.get('petId')
        if senderId is not None and petId is not None:
            try:
                return AdoptionRequest.objects.get(sender_id=senderId,pet_id=petId)
            except:
                return None
        return None

    def resolve_all_request(self,info):
        return AdoptionRequest.objects.all()

    def resolve_favorite_owner_pets(self,info,**kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Pet.objects.filter(likes__id=id)
