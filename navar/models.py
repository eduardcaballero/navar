from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    id_usuario = models.UUIDField(primary_key=True, help_text="ID unico de usuario")
    nombres = models.CharField(max_length=35)
    apellidos = models.CharField(max_length=35)
    cedula = models.CharField(max_length=15)
    contrasena = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=40)
    habilidades = models.TextField()
    correo = models.CharField(max_length=60)
    telefono = models.CharField(max_length=10)

    def __str__(self):
        return self.nombres

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title