from django.db import models
from django.core.validators import EmailValidator
from .validators import validar_rut

class Contacto(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=10, unique=True, validators=[validar_rut])  # unique constraint added
    email = models.EmailField(validators=[EmailValidator(message='Correo electrónico inválido.')], unique=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    comuna = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.DecimalField(max_digits=15, decimal_places=0)  # Assuming numeric without decimal
    mensaje = models.TextField()
    reg_date = models.DateTimeField(auto_now=True)  # auto_now sets the date on update

    class Meta:
        db_table = 'contactos'  # Optional: This defines the table name in the database

    def __str__(self):
        #return f'{self.nombres} {self.apellidos} {self.rut} {self.email} {self.direccion} {self.comuna} {self.telefono} {self.mensaje}'
        return f'{self.nombres} {self.apellidos}'
    
   

    