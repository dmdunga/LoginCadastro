# Generated by Django 4.0.3 on 2022-03-29 16:35

import datetime
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('CPF', models.CharField(max_length=25, verbose_name='CPF')),
                ('cnpj', models.CharField(default=False, max_length=25, verbose_name='cnpj')),
                ('cep', models.CharField(default=False, max_length=25, verbose_name='cep')),
                ('rua', models.CharField(default=False, max_length=25, verbose_name='rua')),
                ('numero', models.CharField(default=False, max_length=10, verbose_name='numero')),
                ('complemento', models.CharField(default=False, max_length=50, verbose_name='complemento')),
                ('bairro', models.CharField(default=False, max_length=25, verbose_name='bairro')),
                ('cidade', models.CharField(default=False, max_length=25, verbose_name='cidade')),
                ('estado', models.CharField(default=False, max_length=25, verbose_name='estado')),
                ('BithDate', models.DateField(default=datetime.date.today, verbose_name='Bith date')),
                ('Phone', models.CharField(max_length=15)),
                ('username', models.CharField(help_text='Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters', max_length=15, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'Enter a valid username.', 'invalid')], verbose_name='username')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('Gender', models.CharField(choices=[('1', 'Feminine'), ('2', 'Masculine'), ('3', 'Other')], max_length=14)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]