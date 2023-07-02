from django.db import models

class Menu (models.Model):
    nombre = models.CharField(max_length=20)
    precio = models.IntegerField()

    def __str__(self):
        return self.nombre

class Proveedores (models.Model):
    nombre_completo = models.CharField(max_length=60)
    telefono = models.IntegerField()
    email = models.EmailField()

class Clientes (models.Model):
    nombre_completo = models.CharField(max_length=60)
    telefono =models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"Nombre Completo: {self.nombre_completo} - Telefono {self.telefono} - E-Mail {self.email}"

    
class Empleados (models.Model):
    nombre_completo = models.CharField(max_length=60)
    telefono = models.IntegerField()
    dni = models.IntegerField()



