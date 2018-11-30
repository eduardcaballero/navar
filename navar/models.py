from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, help_text="ID unico de usuario")
    nombres = models.CharField(max_length=35)
    apellidos = models.CharField(max_length=35)
    cedula = models.CharField(max_length=15)
    contrasena = models.CharField(max_length=20)
    especialidad = models.TextField()
    habilidades = models.TextField()
    correo = models.CharField(max_length=60)
    telefono = models.CharField(max_length=10)

    # @receiver(post_save, sender=id_usuario)
    # def update_user_Usuario(sender, instance, created, **kwargs):
    #     if created:
    #         Usuario.objects.create(user=instance)
    #     instance.Usuario.save()

class Propuesta(models.Model):
    id_propuesta = models.AutoField(primary_key=True,  help_text="ID de la solicitud")
    id_usuario= models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    fecha_propuesta = models.DateField(auto_now_add=True)
    area_misional = models.CharField(max_length=20)
    descripcion = models.TextField()
    propuesta_economica = models.IntegerField()
    condiciones_entrega = models.TextField()
    aprobacion = models.BooleanField(default=False)
    fecha_aprobacion = models.DateField()
    fecha_entrega_p = models.DateField()

class Caso(models.Model):
    id_caso = models.AutoField(primary_key=True,  help_text="ID del caso")
    fecha_inicio = models.DateField(auto_now_add=True)
    especialista = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    ips = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    edad = models.CharField(max_length=3)
    artefacto_metalico = models.BooleanField(default=False)
    tiempo_entrega = models.CharField(max_length=3)
    diagnostico = models.TextField()
    procedimiento_q = models.TextField()
    etiologia_congenito = models.BooleanField(default=False)
    etiologia_oncologico = models.BooleanField(default=False)
    etiologia_traumatico = models.BooleanField(default=False)
    zona_superior = models.BooleanField(default=False)
    zona_medio = models.BooleanField(default=False)
    zona_inferior = models.BooleanField(default=False)
    zona_craneo = models.BooleanField(default=False)
    tiempo_agudo = models.BooleanField(default=False)
    tiempo_subagudo = models.BooleanField(default=False)
    tiempo_cronico = models.BooleanField(default=False)
    diam_tornillo_1 = models.CharField(max_length=6,null=True)
    diam_tornillo_2 = models.CharField(max_length=6,null=True)
    diam_tornillo_3 = models.CharField(max_length=6,null=True)
    diam_tornillo_4 = models.CharField(max_length=6,null=True)
    diam_tornillo_otro = models.CharField(max_length=6,null=True)
    recesion_hueso = models.BooleanField(default=False)
    margen_recesion = models.CharField(max_length=6, null=True)
    numero_sujeciones = models.CharField(max_length=2, null=True)
    incisiones_vias = models.TextField()
    planeamiento_q_v = models.BooleanField(default=False)
    planeamiento_q_f = models.BooleanField(default=False)
    biomodelo_pre_v = models.BooleanField(default=False)
    biomodelo_pre_f = models.BooleanField(default=False)
    biomodelo_pos_v = models.BooleanField(default=False)
    biomodelo_pos_f = models.BooleanField(default=False)
    guia_q_v = models.BooleanField(default=False)
    guia_q_f = models.BooleanField(default=False)
    implante_v = models.BooleanField(default=False)
    implante_f = models.BooleanField(default=False)
    observaciones = models.TextField()

class Asignado(models.Model):
    id_suario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.CASCADE)
    id_propuesta = models.ForeignKey(Propuesta, null=False, blank=False, on_delete=models.CASCADE)
    rol= models.CharField(max_length=30)
    fecha_asignado = models.DateField(auto_now_add=True)

class Paquete(models.Model):
    id_paquete = models.AutoField(primary_key=True,  help_text="ID unico de paquete")
    nombre= models.CharField(max_length=100)
    descripcion = models.TextField()

class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True,  help_text="ID unico de comentario")
    id_propuesta = models.ForeignKey(Propuesta, null=False, blank=False, on_delete=models.CASCADE)
    comentario= models.TextField()

class Actividad(models.Model):
    id_actividad = models.AutoField(primary_key=True,  help_text="ID unico de actividad")
    nombre= models.CharField(max_length=100)
    descripcion = models.TextField()

class Requerimiento(models.Model):
    id_requerimiento = models.AutoField(primary_key=True,  help_text="ID unico de requerimiento")
    id_actividad = models.ForeignKey(Actividad, null=False, blank=False, on_delete=models.CASCADE)
    nombre= models.CharField(max_length=100)
    descripcion = models.TextField()

class Parametro(models.Model):
    id_parametro = models.AutoField(primary_key=True,  help_text="ID unico de parametro")
    id_requerimiento = models.ForeignKey(Requerimiento, null=False, blank=False, on_delete=models.CASCADE)
    medicion = models.CharField(max_length=3)
    aprobado = models.BooleanField(default=False)
    rango = models.CharField(max_length=15)

class Tarea(models.Model):
    id_tarea = models.AutoField(primary_key=True,  help_text="ID unico de tarea")
    nombre= models.CharField(max_length=100)
    descripcion = models.TextField()
    
class EntradaSalida(models.Model):
    id_tarea = models.AutoField(primary_key=True,  help_text="ID unico de tarea")
    nombre= models.CharField(max_length=100)
    descripcion = models.TextField()

class Archivo(models.Model):
    id_tarea = models.AutoField(primary_key=True,  help_text="ID unico de tarea")
    nombre= models.CharField(max_length=100)
    descripcion = models.TextField()