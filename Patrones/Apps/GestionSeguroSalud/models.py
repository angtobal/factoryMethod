from django.db import models

# Modelos.
class TipoSeguro(models.Model):

    descripcion = models.CharField(max_length=35)
    estado = models.BooleanField(default=True)

    def DescripcionConEstado(self):
        cadena = "{0} - {1}"
        strEstado = "Activo"

        if self.estado == False:
            strEstado = "Inactivo"

        return cadena.format(self.descripcion, strEstado)

    def __str__(self):
        return self.DescripcionConEstado()


##Clase Factory
class Seguro():

    #Metodo Factory
    def factory(tipo):
        if tipo.pk == 1:
            return SeguroRegular(tipo)
        if tipo.pk == 2:
            return SeguroIndependiente(tipo)
        if tipo.pk == 3:
            return SeguroRiesgoTrabajo(tipo)
        else:
            return tipo

    factory = staticmethod(factory)



# Clases Que entienden de la clase Tipo de Seguro
class SeguroRegular(TipoSeguro):
    def __init__(self,tipo):
        self.pk= tipo.pk
        self.descripcion = tipo.descripcion
        self.dd = 100

class SeguroIndependiente(TipoSeguro):
    def __init__(self,tipo):
        self.pk= tipo.pk
        self.descripcion = tipo.descripcion
        self.dd = 80.5

class SeguroRiesgoTrabajo(TipoSeguro):
    def __init__(self,tipo):
        self.pk= tipo.pk
        self.descripcion = tipo.descripcion
        self.dd = 5.0

class SeguroPescador(TipoSeguro):
    def __init__(self,tipo):
        self.pk= tipo.pk
        self.descripcion = tipo.descripcion
        self.dd = 1.0