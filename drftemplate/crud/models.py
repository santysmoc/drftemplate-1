from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=120, verbose_name='Nombre')
    last_name = models.CharField(max_length=120, verbose_name='Apellido')
    age = models.IntegerField(default=0, verbose_name='Edad')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Creacion')
    status = models.BooleanField(default=True, verbose_name='status')

    class Meta:
        db_table = 'persons'


class Rol(models.Model):
    name = models.CharField(max_length=120, verbose_name= 'nombre')
    employer = models.CharField(max_length=120, verbose_name= 'employer')
    applicant = models.CharField(max_length=120, verbose_name= 'applicant')

    
    class Meta:
        db_table = 'roles'
#Tabla de rol copiada tal cual.

class User(models.Model):
    email = models.EmailField(max_length=120, verbose_name= 'Email')
    password = models.CharField(max_length=120, verbose_name= 'Pasword')
    rol_id = models.ForeignKey(on_delete=models.CASCADE, verbose_name= 'Rol')

    class Meta:
        db_table = 'users'
 #Tabla de usuario como imagino que es. NO sé si los datos de rol_id están completos o les falta o sobra

class Rol(models.Model):
    name = models.CharField(null=True, verbose_name= 'name')
    employer = models.CharField(max_length=120, verbose_name= 'employer')
    applicant = models.CharField(max_length=120, verbose_name= 'applicant')

    class Meta:
        db_table = 'roles'
#Rolo con un cambio en Name, respecto a null true.

class User(models.Model):
    email = models.EmailField(max_length=120, verbose_name= 'Email')
    password = models.CharField(max_length=120, verbose_name= 'Pasword')
    rol_id = models.ForeignKey(Rol, on_delete=models.CASCADE, verbose_name= 'Rol')

    class Meta:
        db_table = 'users'
#User sin rol id, pensando en que para web no se debe especificar pues sólo es para employers.
class Rol(models.Model):
    name = models.BooleanField(null=True, verbose_name= 'name')
    
    class Meta:
        db_table = 'roles'
