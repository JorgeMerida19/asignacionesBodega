from django.db import models

class Empleado(models.Model):
    dpi = models.CharField(max_length=20)
    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    genero = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    fechaNacimiento = models.DateField(max_length=250)
    ocupacion = models.CharField(max_length=250)
    fechaContratacion = models.DateTimeField(auto_now=False)

    def __unicode_(self):
        return self.nombre

    def __str__(self):
        nombreCompleto = self.nombre +" " +self.apellido
        return nombreCompleto

class Bodega(models.Model):
    nombreBodega = models.CharField(max_length=250)
    nombreDepartamente = models.CharField(max_length=250)
    direccion = models.CharField(max_length=250)
    numTelefono = models.CharField(max_length=250)
    fechaRegistro = models.DateTimeField(auto_now=False)

    def __unicode_(self):
        return self.nombreBodega

class AsignacionBodega(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    nombreAsignacion= models.CharField(max_length=250)
    fecha = models.DateTimeField(auto_now=False)

    def __unicode_(self):
        return self.nombreAsignacion

