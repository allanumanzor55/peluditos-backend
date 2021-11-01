import graphene

from backend_app.models import *
from .types import *

#Mutations de Modulos
class ModuleInput(graphene.InputObjectType):
    id = graphene.ID()
    name= graphene.String()
    description = graphene.String()

class CreateModule(graphene.Mutation):
    module = graphene.Field(ModuleNode)
    
    class Input:
        module_data = ModuleInput(required=True)

    @staticmethod
    def mutate(root,info,module_data=None):
        module_instance = Module.objects.create(name=module_data.name,description=module_data.description)
        return CreateModule(module=module_instance)

class UpdateModule(graphene.Mutation):
    module = graphene.Field(ModuleNode)

    class Input:
        module_data = ModuleInput(required=True)

    @staticmethod
    def mutate(root,info,module_data=None):
        module_instance = Module.objects.get(pk=module_data.id)
        if module_instance:
            if module_data.name is not None: module_instance.name=module_data.name
            if module_data.description is not None: module_instance.description = module_data.description
            module_instance.save()
            return UpdateModule(module=module_instance)
        return UpdateModule(module=None)

class DeleteModule(graphene.Mutation):
    module = graphene.Field(ModuleNode)

    class Input:
        id =graphene.ID()

    @staticmethod
    def mutate(root,info,id):
        Module.objects.get(pk=id).delete()
        return None


#Mutations de Roles
class RoleInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()

class CreateRole(graphene.Mutation):
    class Input:
        role_data = RoleInput(required=True)
    role = graphene.Field(RoleNode)

    @staticmethod
    def mutate(root,info,role_data=None):
        obj = Role.objects.create(name=role_data.name,description=role_data.description)
        return CreateRole(role=obj)

class UpdateRole(graphene.Mutation):
    role = graphene.Field(RoleNode)
    class Input:
        role_data = RoleInput(required=True)

    @staticmethod
    def mutate(root,info,role_data=None):
        role_instance = Role.objects.get(pk=role_data.id)
        if role_instance:
            if role_data.name is not None: role_instance.name = role_data.name
            if role_data.description is not None: role_instance.description = role_data.description
            role_instance.save()
            return UpdateRole(role=role_instance)
        return UpdateRole(role=None)

class DeleteRole(graphene.Mutation):
    role = graphene.Field(RoleNode)

    class Input:
        id = graphene.ID()

    @staticmethod
    def mutate(root,info,id):
        Role.objects.get(pk=id).delete()
        return None

#Mutations de Tipos de perfil
class ProfileTypeInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    description = graphene.String()

class CreateProfileType(graphene.Mutation):
    profileType = graphene.Field(ProfileTypeNode)
    class Input:
        profile_type_data= ProfileTypeInput(required=True)
        
    @staticmethod
    def mutate(root,info,profile_type_data=None):
        profileType_instance = ProfileType.objects.create(
            profileName=profile_type_data.name,description=profile_type_data.description)
        return CreateProfileType(profileType=profileType_instance)

class DeleteProfileType(graphene.Mutation):
    ProfileType = graphene.Field(ProfileTypeNode)

    class Input:
        id = graphene.ID()

    @staticmethod
    def mutate(root,info,id):
        ProfileType.object.get(pk=id).delete()
        return None

#Mutations de Permisos
class PermissionsInput(graphene.InputObjectType):
    id = graphene.ID()
    role_id = graphene.Int()
    module_id = graphene.Int()
    create = graphene.Boolean()
    read = graphene.Boolean()
    update = graphene.Boolean()
    delete = graphene.Boolean()
    
class CreatePermissions(graphene.Mutation):
    permission = graphene.Field(PermissionsNode)
    class Input:
        permission_data = PermissionsInput(required=True)

    @staticmethod
    def mutate(root,info,permission_data=None):
        obj = Permissions.objects.create(
            role_id=permission_data.role_id,
            module_id=permission_data.module_id,
            create=permission_data.create,
            read=permission_data.read,
            update=permission_data.update,
            delete=permission_data.delete)
        return CreatePermissions(permission=obj)

class UpdatePermission(graphene.Mutation):
    permission = graphene.Field(PermissionsNode)
    
    class Input:
        perm_data = PermissionsInput(required=True)

    @staticmethod
    def mutate(root,info,perm_data=None):
        perm_instance = Permissions.objects.get(module_id=perm_data.module_id,role_id=perm_data.role_id)
        if perm_instance:
            if perm_data.create is not None: perm_instance.create = perm_data.create
            if perm_data.read is not None: perm_instance.read = perm_data.read
            if perm_data.update is not None: perm_instance.update = perm_data.update
            if perm_data.delete is not None: perm_instance.delete = perm_data.delete
            perm_instance.save()
            return UpdatePermission(permission=perm_instance)
        return UpdatePermission(permission=None)

class DeletePermission(graphene.Mutation):
    permission = graphene.Field(PermissionsNode)

    class Input:
        id = graphene.ID()

    @staticmethod
    def mutate(root,info,id):
        Permissions.object.get(pk=id).delete()
        return None

#Mutations de Usuarios
class AddressInput(graphene.InputObjectType):
    department = graphene.String()
    city = graphene.String()
    suburb = graphene.String()
    street = graphene.String()
    residence = graphene.String()
    reference = graphene.String()

class UserInput(graphene.InputObjectType):
    id = graphene.ID()
    role_id = graphene.Int()
    profileType_id = graphene.Int()
    email = graphene.String()
    password = graphene.String()
    firstName = graphene.String()
    lastName = graphene.String()
    dni = graphene.String()
    age = graphene.String()
    principalCellphone = graphene.String()
    auxiliarCellphone = graphene.String()
    address = AddressInput(required=True)

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserNode)

    class Input:
        user_data = UserInput(required=True)
    
    @staticmethod
    def mutate(root,info,user_data=None):
        address_instance = Address.objects.create(
            department=user_data.address.department,
            city=user_data.address.city,
            suburb=user_data.address.suburb,
            street=user_data.address.street,
            residence=user_data.address.residence,
            reference=user_data.address.reference
        )
        user_instance = User.objects.create(
            role_id = user_data.role_id,
            profileType_id=user_data.profileType_id,
            address = address_instance,
            email=user_data.email,
            password=user_data.password,
            firstName=user_data.firstName,
            lastName=user_data.lastName,
            dni=user_data.dni,
            age=user_data.age,
            principalCellphone=user_data.principalCellphone,
            auxiliarCellphone=user_data.auxiliarCellphone
        )
        return CreateUser(user=user_instance)

class UpdateUser(graphene.Mutation):
    user = graphene.Field(UserNode)
    class input:
        user_data = UserInput(required=True)

    @staticmethod
    def mutate(root,info,user_data=None):
        user_instance = User.objects.get(pk=user_data.id)
        if user_instance:
            if user_data.email is not None: user_instance.email=user_data.email
            if user_data.password is not None: user_instance.password=user_data.password
            if user_data.firstName is not None: user_instance.firstName=user_data.firstName
            if user_data.lastName is not None: user_instance.lastName=user_data.lastName
            if user_data.dni is not None: user_instance.dni=user_data.dni
            if user_data.age is not None: user_instance.age=user_data.age
            if user_data.principalCellPhone is not None: 
                user_instance.principalCellPhone=user_data.principalCellPhone
            if user_data.auxiliarCellphone is not None: 
                user_instance.auxiliarCellphone=user_data.auxiliarCellphone
            user_instance.save()
            return UpdateUser(user=user_instance)
        return UpdateUser(user=None)

class DeleteUser(graphene.Mutation):
    user = graphene.Field(UserNode)
    class Input:
        id = graphene.ID()

    @staticmethod
    def mutate(root,info,id):
        User.objects.get(pk=id).delete()
        return None

#Mutations de Categorias de mascotas
class CreatePetCategory(graphene.Mutation):
    petCategory = graphene.Field(PetCategoryNode)
    class Input:
        name = graphene.String()
    
    @staticmethod
    def mutate(root,info,name):
        petCategory_instance = PetCategory.objects.create(name=name)
        return CreatePetCategory(petCategory=petCategory_instance)

class UpdatePetCategory(graphene.Mutation):
    petCategory = graphene.Field(PetCategoryNode)
    class Input:
        id = graphene.ID()
        name = graphene.String()
    
    @staticmethod
    def mutate(root,info,id,name):
        petCategory_instance = PetCategory.objects.get(pk=id)
        if petCategory_instance:
            if name is not None: petCategory_instance.name = name
            return UpdatePetCategory(petCategory=petCategory_instance)
        return UpdatePetCategory(petCategory=None)

class DeletePetCategory(graphene.Mutation):
    petCategory = graphene.Field(PetCategoryNode)
    class Input:
        id = graphene.ID()

    @staticmethod
    def mutate(root,info,id):
        PetCategory.objects.delete(pk=id)
        return None

#Mutations de Vacunas de mascotas
class CreateVaccine(graphene.Mutation):
    vaccine = graphene.Field(VaccineNode)
    class Input:
        name = graphene.String()
    
    @staticmethod
    def mutate(root,info,name):
        vaccine_instance = Vaccine.objects.create(name=name)
        return CreateVaccine(vaccine=vaccine_instance)

class UpdateVaccine(graphene.Mutation):
    vaccine = graphene.Field(VaccineNode)
    class Input:
        id = graphene.ID()
        name = graphene.String()
    
    @staticmethod
    def mutate(root,info,id,name):
        vaccine_instance = Vaccine.objects.get(pk=id)
        if vaccine_instance:
            if name is not None: vaccine_instance.name = name
            return UpdateVaccine(vaccine=vaccine_instance)
        return UpdateVaccine(vaccine=None)

class DeleteVaccine(graphene.Mutation):
    vaccine = graphene.Field(VaccineNode)
    class Input:
        id = graphene.ID()

    @staticmethod
    def mutate(root,info,id):
        Vaccine.objects.delete(pk=id)
        return None

#Mutations de Mascotas

class PetInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    category_id = graphene.Int()
    owner_id = graphene.Int()
    birthDate = graphene.String()
    breed = graphene.String()
    color = graphene.String()
    size = graphene.String()
    gender = graphene.String()
    isSterilized = graphene.String()
    isAdopted = graphene.String()

class CreatePet(graphene.Mutation):
    pet = graphene.Field(PetNode)
    class Input:
        pet_data = PetInput(required=True)
    
    @staticmethod
    def mutate(root,info,**kwargs):
        pet_instance = Pet.objects.create(
            name = pet_data.name,
            category_id=pet_data.category_id,
            owner_id=pet_data.owner_id,
            birthDate=pet_data.birthDate,
            breed=pet_data.breed,
            color=pet_data.color,
            size=pet_data.size,
            gender=pet_data.gender,
            isSterilized=pet_data.isSterilized,
            isAdopted=pet_data.isAdopted
        )
        return CreatePet(pet=pet_instance)

# class UpdatePet(graphene.Mutation):
#     @staticmethod
#     def mutate(root,info,**kwargs):
#         pass

class DeletePet(graphene.Mutation):
    pet = graphene.Field(PetNode)
    class Input:
        id = graphene.ID()
    
    @staticmethod
    def mutate(root,info,id):
        Pet.objects.delete(pk=id)
        return None

class Mutation(graphene.AbstractType):
    create_module = CreateModule.Field()
    update_module = UpdateModule.Field()
    delete_module = DeleteModule.Field()
    create_role = CreateRole.Field()
    update_role = UpdateRole.Field()
    delete_role = DeleteRole.Field()
    create_profile_type = CreateProfileType.Field()
    create_permissions = CreatePermissions.Field()
    update_permissions = UpdatePermission.Field()
    delete_permissions = DeletePermission.Field()
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()
    create_pet_category = CreatePetCategory.Field()
    update_pet_category = UpdatePetCategory.Field()
    delete_pet_category = DeletePetCategory.Field()
    create_vaccine = CreateVaccine.Field()
    update_vaccine = UpdateVaccine.Field()
    delete_vaccine = DeleteVaccine.Field()
    create_pet = CreatePet.Field()
    # update_pet = UpdatePet.Field()
    delete_pet = DeletePet.Field()