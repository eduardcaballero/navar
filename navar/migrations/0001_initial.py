# Generated by Django 2.1.3 on 2018-11-29 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id_actividad', models.UUIDField(help_text='ID unico de actividad', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id_tarea', models.UUIDField(help_text='ID unico de tarea', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Asignado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=30)),
                ('fecha_asignado', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Caso',
            fields=[
                ('id_caso', models.UUIDField(help_text='ID del caso', primary_key=True, serialize=False)),
                ('fecha_inicio', models.DateField(auto_now_add=True)),
                ('ips', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=1)),
                ('edad', models.CharField(max_length=3)),
                ('artefacto_metalico', models.BooleanField(default=False)),
                ('tiempo_entrega', models.CharField(max_length=3)),
                ('diagnostico', models.TextField()),
                ('procedimiento_q', models.TextField()),
                ('etiologia_congenito', models.BooleanField(default=False)),
                ('etiologia_oncologico', models.BooleanField(default=False)),
                ('etiologia_traumatico', models.BooleanField(default=False)),
                ('zona_superior', models.BooleanField(default=False)),
                ('zona_medio', models.BooleanField(default=False)),
                ('zona_inferior', models.BooleanField(default=False)),
                ('zona_craneo', models.BooleanField(default=False)),
                ('tiempo_agudo', models.BooleanField(default=False)),
                ('tiempo_subagudo', models.BooleanField(default=False)),
                ('tiempo_cronico', models.BooleanField(default=False)),
                ('diam_tornillo_1', models.CharField(max_length=6, null=True)),
                ('diam_tornillo_2', models.CharField(max_length=6, null=True)),
                ('diam_tornillo_3', models.CharField(max_length=6, null=True)),
                ('diam_tornillo_4', models.CharField(max_length=6, null=True)),
                ('diam_tornillo_otro', models.CharField(max_length=6, null=True)),
                ('recesion_hueso', models.BooleanField(default=False)),
                ('margen_recesion', models.CharField(max_length=6, null=True)),
                ('numero_sujeciones', models.CharField(max_length=2, null=True)),
                ('incisiones_vias', models.TextField()),
                ('planeamiento_q_v', models.BooleanField(default=False)),
                ('planeamiento_q_f', models.BooleanField(default=False)),
                ('biomodelo_pre_v', models.BooleanField(default=False)),
                ('biomodelo_pre_f', models.BooleanField(default=False)),
                ('biomodelo_pos_v', models.BooleanField(default=False)),
                ('biomodelo_pos_f', models.BooleanField(default=False)),
                ('guia_q_v', models.BooleanField(default=False)),
                ('guia_q_f', models.BooleanField(default=False)),
                ('implante_v', models.BooleanField(default=False)),
                ('implante_f', models.BooleanField(default=False)),
                ('observaciones', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id_comentario', models.UUIDField(help_text='ID unico de comentario', primary_key=True, serialize=False)),
                ('comentario', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EntradaSalida',
            fields=[
                ('id_tarea', models.UUIDField(help_text='ID unico de tarea', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id_paquete', models.UUIDField(help_text='ID unico de paquete', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id_parametro', models.UUIDField(help_text='ID unico de parametro', primary_key=True, serialize=False)),
                ('medicion', models.CharField(max_length=3)),
                ('aprobado', models.BooleanField(default=False)),
                ('rango', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Propuesta',
            fields=[
                ('id_propuesta', models.UUIDField(help_text='ID de la solicitud', primary_key=True, serialize=False)),
                ('fecha_propuesta', models.DateField(auto_now_add=True)),
                ('area_misional', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
                ('propuesta_economica', models.IntegerField()),
                ('condiciones_entrega', models.TextField()),
                ('aprobacion', models.BooleanField(default=False)),
                ('fecha_aprobacion', models.DateField()),
                ('fecha_entrega_p', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Requerimiento',
            fields=[
                ('id_requerimiento', models.UUIDField(help_text='ID unico de requerimiento', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('id_actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navar.Actividad')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id_tarea', models.UUIDField(help_text='ID unico de tarea', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.UUIDField(help_text='ID unico de usuario', primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=35)),
                ('apellidos', models.CharField(max_length=35)),
                ('cedula', models.CharField(max_length=15)),
                ('contrasena', models.CharField(max_length=20)),
                ('especialidad', models.CharField(max_length=40)),
                ('habilidades', models.TextField()),
                ('correo', models.CharField(max_length=60)),
                ('telefono', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='propuesta',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navar.Usuario'),
        ),
        migrations.AddField(
            model_name='parametro',
            name='id_requerimiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navar.Requerimiento'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='id_propuesta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navar.Propuesta'),
        ),
        migrations.AddField(
            model_name='caso',
            name='especialista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navar.Usuario'),
        ),
        migrations.AddField(
            model_name='asignado',
            name='id_propuesta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navar.Propuesta'),
        ),
        migrations.AddField(
            model_name='asignado',
            name='id_suario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='navar.Usuario'),
        ),
    ]
