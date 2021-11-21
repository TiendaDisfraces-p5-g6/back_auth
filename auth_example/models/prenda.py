from django.db                   import models

class Prenda(models.Model):
    id          = models.AutoField(primary_key=True)
    tipo_prenda = models.CharField(max_length=12)
    descripcion = models.CharField(max_length=100)
    talla       = models.CharField(max_length= 3)
    cantidad    = models.IntegerField(default=0)