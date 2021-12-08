import graphene
from smtplib import SMTP
from email.mime.text import MIMEText
from backend_app.models import *
from .types import *
from uuid import uuid4


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
        name = graphene.String()
        description = graphene.String()
        
    @staticmethod
    def mutate(root,info,name,description):
        profileType_instance = ProfileType.objects.create(name=name,description=description)
        return CreateProfileType(profileType=profileType_instance)

class DeleteProfileType(graphene.Mutation):
    profileType = graphene.Field(ProfileTypeNode)

    class Input:
        id = graphene.ID()

    @staticmethod
    def mutate(root,info,id):
        ProfileType.objects.get(pk=id).delete()
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
    biography = graphene.String()
    motto = graphene.String()
    address = AddressInput(required=True)
    verified = graphene.Boolean()
    active = graphene.Boolean()
    secureQuestion = graphene.String()
    secureAnswer = graphene.String()

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
    msg = graphene.String()
    verified = graphene.Boolean()
    class Input:
        user_data = UserInput(required=True)

    @staticmethod
    def mutate(root,info,user_data=None):
        try:
            user_instance = User.objects.get(pk=user_data.id)
            if user_instance:
                if user_data.password is not None: user_instance.password=user_data.password
                if user_data.email is not None: user_instance.email=user_data.email
                if user_data.password is not None: user_instance.password=user_data.password
                if user_data.firstName is not None: user_instance.firstName=user_data.firstName
                if user_data.lastName is not None: user_instance.lastName=user_data.lastName
                if user_data.dni is not None: user_instance.dni=user_data.dni
                if user_data.age is not None: user_instance.age=user_data.age
                if user_data.principalCellphone is not None: 
                    user_instance.principalCellphone=user_data.principalCellphone
                if user_data.auxiliarCellphone is not None: 
                    user_instance.auxiliarCellphone=user_data.auxiliarCellphone
                if user_data.verified is not None: user_instance.verified=user_data.verified
                if user_data.active is not None: user_instance.active = user_data.active
                if user_data.biography is not None: user_instance.biography = user_data.biography
                if user_data.motto is not None: user_instance.motto = user_data.motto
                user_instance.save()
                return UpdateUser(user=user_instance,msg="Correcto",verified=True)
        except Exception as ex: 
            return UpdateUser(user=user_instance,msg=str(ex),verified=False)

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
            petCategory_instance.save()
            return UpdatePetCategory(petCategory=petCategory_instance)
        return UpdatePetCategory(petCategory=None)

class DeletePetCategory(graphene.Mutation):
    petCategory = graphene.Field(PetCategoryNode)
    class Input:
        id = graphene.ID()

    @staticmethod
    def mutate(root,info,id):
        PetCategory.objects.get(pk=id).delete()
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
            vaccine_instance.save()
            return UpdateVaccine(vaccine=vaccine_instance)
        return UpdateVaccine(vaccine=None)

class DeleteVaccine(graphene.Mutation):
    vaccine = graphene.Field(VaccineNode)
    class Input:
        id = graphene.ID()

    @staticmethod
    def mutate(root,info,id):
        Vaccine.objects.get(pk=id).delete()
        return None

#Mutations de razas de mascotas

class CreateBreed(graphene.Mutation):
    breed = graphene.Field(BreedNode)
    class Input:
        name = graphene.String()
    
    @staticmethod
    def mutate(root,info,name):
        breed_instance = Breed.objects.create(name=name)
        return CreateBreed(breed=breed_instance)

class UpdateBreed(graphene.Mutation):
    breed = graphene.Field(BreedNode)
    class Input:
        id = graphene.ID()
        name = graphene.String()
    
    @staticmethod
    def mutate(root,info,id,name):
        breed_instance = Breed.objects.get(pk=id)
        breed_instance.name = name
        breed_instance.save()
        return UpdateBreed(breed=breed_instance)

class DeleteBreed(graphene.Mutation):
    breed = graphene.Field(BreedNode)
    class Input:
        id = graphene.ID()
    
    @staticmethod
    def mutate(root,info,id):
        Breed.objects.get(pk=id).delete()
        return None

#Mutations de Mascotas

class PetInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    category_id = graphene.Int()
    owner_id = graphene.Int()
    birthDate = graphene.String()
    breed_id = graphene.String()
    color = graphene.String()
    size = graphene.String()
    gender = graphene.String()
    isSterilized = graphene.Boolean()
    isAdopted = graphene.Boolean()
    vaccines = graphene.List(graphene.String)
    description = graphene.String()

class CreatePet(graphene.Mutation):
    pet = graphene.Field(PetNode)
    verified = graphene.Boolean()
    class Input:
        pet_data = PetInput(required=True)
    
    @staticmethod
    def mutate(root,info,pet_data):
        try:
            pet_instance = Pet.objects.create(
            name = pet_data.name,
            category_id=pet_data.category_id,
            owner_id=pet_data.owner_id,
            birthDate=pet_data.birthDate,
            breed_id=pet_data.breed_id,
            color=pet_data.color,
            size=pet_data.size,
            gender=pet_data.gender,
            isSterilized=pet_data.isSterilized,
            isAdopted=False,
            description = pet_data.description
            )
            return CreatePet(pet=pet_instance,verified=True)
        except:
            return CreatePet(pet=None,verified=False)

class UpdatePet(graphene.Mutation):
    verified=graphene.Boolean()
    @staticmethod
    class Input:
        pet_data = PetInput(required=True)

    def mutate(root,info,pet_data):
        try:
            pet_instance = Pet.objects.get(pk=pet_data.id)
        except:
            return UpdatePet(verified=False)
        if pet_instance:
            
            if pet_data.name is not None: pet_instance.name = pet_data.name
            if pet_data.category_id is not None: pet_instance.category_id = pet_data.category_id
            if pet_data.birthDate is not None: pet_instance.birthDate = pet_data.birthDate
            if pet_data.breed_id is not None: pet_instance.breed_id = pet_data.breed_id
            if pet_data.color is not None: pet_instance.color = pet_data.color
            if pet_data.size is not None: pet_instance.size = pet_data.size
            if pet_data.gender is not None: pet_instance.gender = pet_data.gender
            if pet_data.isSterilized is not None: pet_instance.isSterilized = str(pet_data.isSterilized)
            if pet_data.isAdopted is not None: pet_instance.isAdopted = str(pet_data.isAdopted)
            pet_instance.save()
            return UpdatePet(verified=True)

class DeletePet(graphene.Mutation):
    verified=graphene.Boolean()
    msg = graphene.String()
    class Input:
        id = graphene.ID()
    
    @staticmethod
    def mutate(root,info,id):
        try:
            Pet.objects.get(pk=id).delete()
            return DeletePet(verified=True,msg="Exito")
        except x:
            return DeletePet(verified=False,msg=x)


class Login(graphene.Mutation):
    verified = graphene.Boolean()
    user = graphene.Field(UserNode)
    class Input:
        email = graphene.String()
        password = graphene.String()
    @staticmethod
    def mutate(root,info,email,password):
        try:
            user_instance = User.objects.get(email=email,password=password)
        except:
            return Login(verified=False,user=None)
        if user_instance:
            if user_instance.active:
                token = uuid4()
                user_instance.token=token
                user_instance.save()
                return Login(verified=True,user=user_instance)
            return Login(verified=False,user=user_instance)

class TryLogin(graphene.Mutation):
    verified = graphene.Boolean()
    user = graphene.Field(UserNode)
    class Input:
        email = graphene.String()
        password = graphene.String()
    @staticmethod
    def mutate(root,info,email,password):
        try:
            user_instance = User.objects.get(email=email,password=password)
            if user_instance:
                return Login(verified=True,user=user_instance)
        except:
            return Login(verified=False,user=None)
        

class VerifyLogin(graphene.Mutation):
    verified = graphene.Boolean()
    class Input:
        token = graphene.String()
        id=graphene.ID()
    @staticmethod
    def mutate(root,info,token,id):
        try:
            user_instance = User.objects.get(token__exact=token,pk=id)
            if user_instance:
                return VerifyLogin(verified=True)
            return VerifyLogin(verified=False)
        except:
            return VerifyLogin(verified=False)
        

class Logout(graphene.Mutation):
    verified=graphene.Boolean()
    class Input:
        token = graphene.String()
    def mutate(root,info,token):
        user_instance = User.objects.get(token=token)
        if user_instance:
            user_instance.token=""
            user_instance.save()
            return Logout(verified=True)
        return Logout(verified=False)


class Register(graphene.Mutation):
    user = graphene.Field(UserNode)
    register = graphene.Boolean()

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
            profileType_id= 2,
            address = address_instance,
            email=user_data.email,
            password=user_data.password,
            firstName=user_data.firstName,
            lastName=user_data.lastName,
            dni=user_data.dni,
            age=user_data.age,
            principalCellphone=user_data.principalCellphone,
            auxiliarCellphone=user_data.auxiliarCellphone,
            verified = False,
            secureQuestion = user_data.secureQuestion,
            secureAnswer = user_data.secureAnswer,
            token = uuid4()
        )
        if user_instance:
            return Register(user=user_instance,register=True)
        return Register(register=False)

class UserInfo(graphene.Mutation):
    adoptedPets = graphene.Int()
    adoptionPets = graphene.Int()
    requestsSent = graphene.Int()
    requestsAwait = graphene.Int()
    class Input:
        id = graphene.Int()
    
    @staticmethod
    def mutate(root,info,id):
        try:
            adoptedPets = Pet.objects.filter(owner_id=id).filter(isAdopted__icontains=True).count()
            adoptionPets = Pet.objects.filter(owner_id=id).filter(isAdopted__icontains=False).count()
            requestSent = AdoptionRequest.objects.filter(user_id=id).count()
            requestAwait = AdoptionRequest.objects.filter(user_id=id).filter(accepted__icontains=False).count()
            return UserInfo(adoptedPets=adoptedPets,adoptionPets=adoptionPets,requestsSent=requestSent,requestsAwait=requestAwait)
        except:
            return UserInfo(adoptedPets=0,adoptionPets=0,requestsSent=0,requestsAwait=0)

class RestorePassword(graphene.Mutation):
    verified = graphene.Boolean()
    msg = graphene.String()
    class Input:
        email = graphene.String()
        dni = graphene.String()
        answer = graphene.String()
    
    @staticmethod
    def mutate(root,info,email,dni,answer):
        try:
            us_ins = User.objects.get(email=email,dni=dni)
        except:
            return RestorePassword(verified=False,msg="Datos incorrectos")
        if us_ins:
            if us_ins.secureAnswer == answer:
                try:
                    remitente = "allanalvarez55@gmail.com"
                    destinatario = us_ins.email
                    asunto="Envio de contraseña por email"
                    mensaje="""
                        Hola! %s %s <br/>
                        Te enviamos tu contraseña: <b> %s </b>
                    """%(us_ins.firstName,us_ins.lastName,us_ins.password)
                    mail = MIMEText(mensaje, "html",_charset="utf-8")
                    mail["From"] = remitente
                    mail["To"] = destinatario
                    mail["Subject"] = asunto
                    smtp = SMTP("smtp.gmail.com")
                    smtp.starttls()
                    smtp.login(remitente,"Condemilenario")
                    smtp.sendmail(remitente, destinatario, mail.as_string())
                    smtp.quit()
                    return RestorePassword(verified=True,msg="Verificacion correcta, se envio la contraseña a tu correo")
                except Exception  as ex:
                    return RestorePassword(verified=False,msg=ex)
            return RestorePassword(verified=False,msg="Alguno de los datos ingresados estan incorrectos")

class Like(graphene.Mutation):
    verified = graphene.Boolean()
    msg = graphene.String()
    class Input:
        user = graphene.ID()
        pet = graphene.ID()
        like = graphene.Boolean()
    @staticmethod
    def mutate(root,info,user,pet,like):
        try:
            user_instance = User.objects.get(pk=user)
            pet_instance = Pet.objects.get(pk=pet)
            if like:    
                pet_instance.likes.remove(user_instance)
            else:
                pet_instance.likes.add(user_instance)
            return Like(verified=True,msg="Correcto")
        except Exception as ex:
            return  Like(verified=False,msg=str(ex))

class AdoptionRequestInput(graphene.InputObjectType):
    id = graphene.ID()
    sender = graphene.Int()
    receiver = graphene.Int()
    pet = graphene.Int()
    description = graphene.String()

class SendAdoptionRequest(graphene.Mutation):
    verified = graphene.Boolean()
    msg = graphene.String()
    class Input:
        request_data = AdoptionRequestInput(required=True)
    
    @staticmethod
    def mutate(root,info,request_data=None):
        try:
            AdoptionRequest.objects.create(
                sender_id=request_data.sender,
                receiver_id= request_data.receiver,
                pet_id = request_data.pet,
                description = request_data.description
            )
            return SendAdoptionRequest(verified=True)
        except Exception as x:
            return SendAdoptionRequest(verified=False,msg=str(x))

class UpdateStateReceiveRequest(graphene.Mutation):
    verified= graphene.Boolean()
    msg = graphene.String()

    class Input:
        receiver = graphene.Int()
        sender = graphene.Int()
        pet = graphene.Int()
        state = graphene.String()
    
    @staticmethod
    def mutate(root,info,receiver,sender,pet,state):
        try:
            request_instance = AdoptionRequest.objects.get(receiver=receiver,sender=sender,pet=pet)
            request_instance.state=state
            request_instance.save()
            return UpdateStateReceiveRequest(verified=True,msg="Correcto")
        except Exception as ex: 
            return UpdateStateReceiveRequest(verified=False,msg=str(ex))

class UpdateRequest(graphene.Mutation):
    verified = graphene.Boolean()
    msg = graphene.String()
    class Input:
        id = graphene.ID()
        state = graphene.String()
    @staticmethod
    def mutate(root,info,id,state):
        try:
            adoption_instance = AdoptionRequest.objects.get(pk=id)
            adoption_instance.state = state
            adoption_instance.save()
            return UpdateRequest(verified=True,msg="Correcto")
        except Exception as x:
            return UpdateRequest(verified=True,msg=str(x))

class CancelRequest(graphene.Mutation):
    verified = graphene.Boolean()
    msg = graphene.String()
    class Input:
        idSender = graphene.Int()
        idPet = graphene.Int()
    
    def mutate(root,info,idSender,idPet):
        try:
            AdoptionRequest.objects.get(sender_id=idSender,pet_id=idPet).delete()
            return CancelRequest(verified=True,msg="Eliminado")
        except Exception as ex:
            return CancelRequest(verified=False,msg=str(ex))

class Mutation(graphene.AbstractType):
    create_module = CreateModule.Field()
    update_module = UpdateModule.Field()
    delete_module = DeleteModule.Field()
    create_role = CreateRole.Field()
    update_role = UpdateRole.Field()
    delete_role = DeleteRole.Field()
    create_profile_type = CreateProfileType.Field()
    delete_profile_type = DeleteProfileType.Field()
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
    create_breed = CreateBreed.Field()
    update_breed = UpdateBreed.Field()
    delete_breed = DeleteBreed.Field()
    create_pet = CreatePet.Field()
    update_pet = UpdatePet.Field()
    delete_pet = DeletePet.Field()
    login = Login.Field()
    try_login = TryLogin.Field()
    register = Register.Field()
    user_info = UserInfo.Field()
    verify_login = VerifyLogin.Field()
    logout = Logout.Field()
    restore_password = RestorePassword.Field()
    like = Like.Field()
    send_adoption_request = SendAdoptionRequest.Field()
    update_request = UpdateRequest.Field()
    update_receive_request = UpdateStateReceiveRequest.Field()
    cancel_request = CancelRequest.Field()