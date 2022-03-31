# Generated by Django 3.2.8 on 2022-03-31 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_paciente_profissional'),
        ('app1', '0002_rename_pacienteautorizou_pacientesativo_pacienteautorizouimagem_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientesativo',
            name='Paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.paciente'),
        ),
        migrations.AlterField(
            model_name='pacientesativo',
            name='Profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.profissional'),
        ),
        migrations.AlterField(
            model_name='pesquisasativa',
            name='Profissional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.profissional'),
        ),
        migrations.DeleteModel(
            name='paciente',
        ),
        migrations.DeleteModel(
            name='profissional',
        ),
    ]