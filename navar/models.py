from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    Id_usuario = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico de usuario")
    Nombres = models.CharField(max_length=35)
    Apellidos = models.CharField(max_length=35)
    Cedula = models.CharField(max_length=15)
    Contrasena = models.CharField(max_length=20)
    Especialidad = models.CharField(max_length=40)
    Habilidades = models.TextField()
    Correo = models.CharField(max_length=60)
    Telefono = models.CharField(max_length=10)

class Propuesta(models.Model):
    Id_propuesta = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID de la solicitud")
    Id_usuario= models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    Fecha_propuesta = models.DateField(auto_now_add=True)
    Area_misional = models.CharField(max_length=20)
    Descripcion = models.TextField()
    Propuesta_economica = models.IntegerField()
    Condiciones_entrega = models.TextField()
    Aprobacion = models.BooleanField(default=False)
    Fecha_aprobacion = models.DateField()
    Fecha_entrega_p = models.DateField()

class Caso(models.Model):
    Id_caso = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID del caso")
    Fecha_inicio = models.DateField(auto_now_add=True)
    Especialista = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    Ips = models.CharField(max_length=100)
    SEXOS=(('F','Femenino'),('M','Masculino'))
    Sexo = models.CharField(max_length=1,choise=SEXOS, default='M')
    Edad = models.CharField(max_length=3)
    Artefacto_metalico = models.BooleanField(default=False)
    Tiempo_entrega = models.CharField(max_length=3)
    Diagnostico = models.TextField()
    Procedimiento_q = models.TextField()
    Etiologia_congenito = models.BooleanField(default=False)
    Etiologia_oncologico = models.BooleanField(default=False)
    Etiologia_traumatico = models.BooleanField(default=False)
    Zona_superior = models.BooleanField(default=False)
    Zona_medio = models.BooleanField(default=False)
    Zona_inferior = models.BooleanField(default=False)
    Zona_craneo = models.BooleanField(default=False)
    Tiempo_agudo = models.BooleanField(default=False)
    Tiempo_subagudo = models.BooleanField(default=False)
    Tiempo_cronico = models.BooleanField(default=False)
    Diam_tornillo_1 = models.CharField(max_length=6,null=True)
    Diam_tornillo_2 = models.CharField(max_length=6,null=True)
    Diam_tornillo_3 = models.CharField(max_length=6,null=True)
    Diam_tornillo_4 = models.CharField(max_length=6,null=True)
    Diam_tornillo_otro = models.CharField(max_length=6,null=True)
    Recesion_hueso = models.BooleanField(default=False)
    Margen_recesion = models.CharField(max_length=6, null=True)
    Numero_sujeciones = models.CharField(max_length=2, null=True)
    Incisiones_vias = models.TextField()
    Planeamiento_q_v = models.BooleanField(default=False)
    Planeamiento_q_f = models.BooleanField(default=False)
    Biomodelo_pre_v = models.BooleanField(default=False)
    Biomodelo_pre_f = models.BooleanField(default=False)
    Biomodelo_pos_v = models.BooleanField(default=False)
    Biomodelo_pos_f = models.BooleanField(default=False)
    Guia_q_v = models.BooleanField(default=False)
    Guia_q_f = models.BooleanField(default=False)
    Implante_v = models.BooleanField(default=False)
    Implante_f = models.BooleanField(default=False)
    Observaciones = models.TextField()

class Asignado(models.Model):
    Id_suario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    Id_propuesta = models.ForeignKey(Propuesta, null=False, blank=False, on_delete=models.CASCADE)
    Rol= models.CharField(max_length=30)
    Fecha_asignado = models.DateField(auto_now_add=True)

class Paquete(models.Model):
    Id_paquete = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico de paquete")
    Nombre= models.CharField(max_length=100)
    Descripcion = models.TextField()

class Comentario(models.Model):
    Id_comentario = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico de comentario")
    Id_propuesta = models.ForeignKey(Propuesta, null=False, blank=False, on_delete=models.CASCADE)
    Comentario= models.TextField()

class Actividad(models.Model):
    Id_actividad = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico de actividad")
    Nombre= models.CharField(max_length=100)
    Descripcion = models.TextField()

class Requerimiento(models.Model):
    Id_requerimiento = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico de requerimiento")
    Id_actividad = models.ForeignKey(Actividad, null=False, blank=False, on_delete=models.CASCADE)
    Nombre= models.CharField(max_length=100)
    Descripcion = models.TextField()

class Parametro(models.Model):
    Id_parametro = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico de parametro")
    Id_requerimiento = models.ForeignKey(Requerimiento, null=False, blank=False, on_delete=models.CASCADE)
    Medicion = models.CharField(max_length=3)
    Aprobado = models.BooleanField(default=False)
    Rango = CharField(max_length=15)

class Tarea(models.Model):
    Id_tarea = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico de tarea")
    Nombre= models.CharField(max_length=100)
    Descripcion = models.TextField()
    
class EntradaSalida(models.Model):
    Id_tarea = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico de tarea")
    Nombre= models.CharField(max_length=100)
    Descripcion = models.TextField()

class Archivo(models.Model):
    Id_tarea = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID unico de tarea")
    Nombre= models.CharField(max_length=100)
    Descripcion = models.TextField()

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