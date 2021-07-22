from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

class AdministracionCuentas(BaseUserManager):

    def create_user(self, rut, rutD, email, nombre, password=None ):
        if not rut:
            raise ValueError("Ingresar rut valido")
        if not email:
            raise ValueError("Ingresar correo valido")
        if not nombre:
            raise ValueError("Ingresar nombre valido")
        if not rutD:
            raise ValueError("Ingresar un digito valido")
        user = self.model(
            rut=rut,
            rutD=rutD,
            email=self.normalize_email(email),
            nombre=nombre,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, rut, rutD, email, nombre, password):
        user = self.create_user(
            rut=rut,
            rutD=rutD,
            email=self.normalize_email(email),
            nombre=nombre,
            password=password,
        )
        user.esAdmin  = True
        user.is_staff = True
        user.save(using=self._db)
        return user


def getImagenPerfilPath(self,filename):
    return f'img/{self.pk}/{"foto.jpeg"}'

def getImagenDefault():
    return "media/imagenDefault.png"

#Esta wea es el pulento modelo
class colaborador(AbstractBaseUser):
    email               = models.EmailField(max_length=200, unique=True, verbose_name="email")
    password            = models.CharField(max_length=128, verbose_name="Contraseña")
    fotoPerfil          = models.ImageField(max_length=255, upload_to=getImagenPerfilPath, null=True, blank=True, default=getImagenDefault, verbose_name="Foto de Perfil")
    rut                 = models.CharField(max_length=13, verbose_name="RUT sin digito verificador", primary_key=True)
    rutD                = models.CharField(max_length=1, verbose_name="Verificador RUT")
    nombre              = models.CharField(max_length=200, verbose_name="Nombre")
    fono                = models.CharField(max_length=8, verbose_name="Fono")
    direccion           = models.CharField(max_length=200, verbose_name="Direccion")
    pais                = models.CharField(max_length=20, verbose_name="Pais")
    esAdmin             = models.BooleanField(default=False, verbose_name="Es Administrador?")
    is_staff            = models.BooleanField(default=False, verbose_name="Es parte del proyecto?")

    objects = AdministracionCuentas()

    
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['nombre','rut', 'rutD']

    
    def __str__(self):
        return self.nombre
    
    def sacarNombreImagen(self):
        return str(self.fotoPerfil)[str(self.fotoPerfil).index(f'img/{self.pk}/'):]
    def has_perm(self, perm, obj=None):
        return self.esAdmin
    
    
    def has_module_perms(self, app_label):
        return True

