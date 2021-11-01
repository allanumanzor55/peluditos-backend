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

class PetCategoryNode(DjangoObjectType):
    class Meta:
        model = PetCategory

class VaccineNode(DjangoObjectType):
    class Meta:
        model=Vaccine

class PetNode(DjangoObjectType):
    class Meta:
        model = Pet
        interface = (relay.Node,)


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
    all_pets = graphene.List(PetNode)
    all_pet_categories = graphene.List(PetCategoryNode)
    #Querys ligadas a valores
    permissions = graphene.List(PermissionsNode,roleId=graphene.Int())
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
    get_pets = graphene.List(PetNode,
                            categoryId = graphene.Int(),
                            categoryName=graphene.String(),
                            birthDate=graphene.Date(),
                            breed=graphene.String(),
                            color=graphene.String(),
                            size=graphene.String(),
                            isSterilized=graphene.Boolean(),
                            isAdopted=graphene.Boolean())
    
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
        return Pet.objects.all()

    def resolve_all_pet_categories(self,info,**kwargs):
        return PetCategory.objects.all()

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
            return User.objects.get(pk=idUser)
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
        if firstName and lastName is not None:
            return User.objects.filter(firstName__icontains=firstName)
        elif lastName is not None:
            return User.objects.filter(lastName__icontains=lastName)

    def resolve_pet(self,info,**kwargs):
        idPet = kwargs.get('id')
        petName = kwargs.get('name')
        if idPet is not None:
            return Pet.objects.get(pk=idPet)
        elif petName is not None:
            return Pet.objects.get(name=petName)
    
    def resolve_owner_pets(self,info,**kwargs):
        idOwner = kwargs.get('ownerId')
        ownerFirstName = kwargs.get('firstName')
        ownerFirstName = kwargs.get('firstName')
        if idOwner is not None:
            return Pet.objects.get(owner_id=idOwner)
        elif ownerFirstName is not None:
            return Pet.objects.filter(owner_firstName__icontains=ownerFirstName)
    
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
            return Pet.objects.filter(isAdopted__icontains=isAdopted)    
