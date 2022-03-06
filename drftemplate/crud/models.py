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