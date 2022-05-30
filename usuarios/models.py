import email
from operator import truediv
from pyexpat import model
from xml.etree.ElementInclude import default_loader
from django.db import models
from django.contrib.auth.models import(
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

class UsuarioManager(BaseUserManager):
    
    def create_user(self, email, password):
        usuario = self.model(
            email=self.normalize_email(email)
        )

        usuario.is_active = True
        usuario.is_staff = False
        usuario.is_superuser = False

        usuario.set_password(password)

        usuario.save()

        return usuario

    def create_superuser(self, email, password):
        usuario = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )

        usuario.is_active = True
        usuario.is_staff = True
        usuario.is_superuser = True

        usuario.set_password(password)

        usuario.save()

        return usuario



class Usuario(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(
        verbose_name="E-mail do usuario",
        max_length=194,
        unique=True,
    )

    is_active = models.BooleanField(
        verbose_name="Usuario está ativo",
        default=True,
    )

    is_staff = models.BooleanField(
        verbose_name="Usuario é da equipe de desenvolvimento",
        default=False,
    )

    is_superuser = models.BooleanField(
        verbose_name="Usuario é um superusuario",
        default=False,
    )

    USERNAME_FIELD = "email"

    object = UsuarioManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.email