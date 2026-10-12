from django.db import models

class Destino(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    precio = models.PositiveIntegerField()
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class PaquetesTuristico(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    duracion = models.IntegerField(help_text="Duración en días")
    valor = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre