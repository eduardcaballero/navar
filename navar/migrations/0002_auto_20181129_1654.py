# Generated by Django 2.1.3 on 2018-11-29 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='especialidad',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id_usuario',
            field=models.AutoField(help_text='ID unico de usuario', primary_key=True, serialize=False),
        ),
    ]
