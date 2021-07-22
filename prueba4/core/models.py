from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

#Son las 7:32 de la mañana, tengo frio y me siento solo
class AdministracionCuentas(BaseUserManager):

    def create_user(self, rutNumero, rutDigitoVer, email, nombreCompleto, password=None ):
        if not rutNumero:
            raise ValueError("Porfavor ingresar un rut valido!!")
        if not email:
            raise ValueError("Porfavor ingresar un correo valido!!")
        if not nombreCompleto:
            raise ValueError("Porfavor ingresar un nombre valido!!")
        if not rutDigitoVer:
            raise ValueError("Porfavor ingresar un digito valido!!")
        user = self.model(
            rutNumero=rutNumero,
            rutDigitoVer=rutDigitoVer,
            email=self.normalize_email(email),
            nombreCompleto=nombreCompleto,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rutNumero, rutDigitoVer, email, nombreCompleto, password):
        user = self.create_user(
            rutNumero=rutNumero,
            rutDigitoVer=rutDigitoVer,
            email=self.normalize_email(email),
            nombreCompleto=nombreCompleto,
            password=password,
        )
        user.esAdmin  = True
        user.is_staff = True
        user.save(using=self._db)
        return user


#Seba esta wea define variables
def getImagenPerfilPath(self,filename):
    return f'imagenes/{self.pk}/{"foto.png"}'

def getImagenDefault():
    return "media/imagenDefault.png"

#Esta wea es el pulento modelo
class colaborador(AbstractBaseUser):
    email               = models.EmailField(max_length=200, unique=True, verbose_name="email")
    password            = models.CharField(max_length=128, verbose_name="Contraseña")
    fotoPerfil          = models.ImageField(max_length=255, upload_to=getImagenPerfilPath, null=True, blank=True, default=getImagenDefault, verbose_name="Foto de Perfil")
    rutNumero           = models.CharField(max_length=13, verbose_name="RUT sin digito verificador", primary_key=True)
    rutDigitoVer        = models.CharField(max_length=1, verbose_name="Digito verificador RUT")
    nombreCompleto      = models.CharField(max_length=200, verbose_name="Nombre")
    fonoTelefonico      = models.CharField(max_length=8, verbose_name="Fono")
    direccion           = models.CharField(max_length=200, verbose_name="Direccion de Residencia")
    paisResidencia      = models.CharField(max_length=20, verbose_name="Pais Residente")
    esAdmin             = models.BooleanField(default=False, verbose_name="Tiene privilegios de Administrador?")
    is_staff            = models.BooleanField(default=False, verbose_name="Es de parte del proyecto?")

    objects = AdministracionCuentas()

    #hace que muestre el nombre en vez del correo
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['nombreCompleto','rutNumero', 'rutDigitoVer']

    
    def __str__(self):
        return self.nombreCompleto
    
    def sacarNombreImagen(self):
        return str(self.fotoPerfil)[str(self.fotoPerfil).index(f'imagenes/{self.pk}/'):]
    #lo hice para hacerme mas facil la vida perdoname por el amor de jesucristo
    def has_perm(self, perm, obj=None):
        return self.esAdmin
    
    
    def has_module_perms(self, app_label):
        return True

