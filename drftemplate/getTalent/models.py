from django.db import models

# Create your models here.

class User(models.Model):
    email = models.EmailField(max_length=120, verbose_name='Email')
    password = models.CharField(max_length=120, verbose_name='Password')
    APPLICANT = 1
    EMPLOYER = 2
    ROLES = [
        (APPLICANT, ('Looking for a job')),
        (EMPLOYER, ('Looking for an employee')),    
    ]
    rol = models.CharField(max_length=120, choices=ROLES, verbose_name='Rol')

    class Meta:
        db_table = 'users'

''' datos ejemplo para practicar registro de usuaria
{
"email":"irlandakelly@gmail.com",
"password":"123456",
"rol_id":"1"
}
'''
