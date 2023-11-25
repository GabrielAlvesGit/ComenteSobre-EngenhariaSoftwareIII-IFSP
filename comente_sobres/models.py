from django.db import models
from unidecode import unidecode
from django.db import models

class Usuario(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name

class Topico(models.Model):
    name = models.CharField(max_length=200)
    name_unaccented = models.CharField(max_length=200, editable=False)
    date_added = models.DateTimeField(auto_now_add=True)
    usuario_added = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)

    def save(self, *args, **kwargs):
        self.name_unaccented = unidecode(self.name).lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Comentario(models.Model):
    texto = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    curtidas = models.IntegerField(default=0)
    id_usuario_added = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_topico = models.ForeignKey(Topico, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto