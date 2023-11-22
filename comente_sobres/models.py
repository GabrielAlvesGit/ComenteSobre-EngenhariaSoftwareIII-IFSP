from django.db import models

from django.db import models

class Usuario(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name

class Topico(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    usuario_added = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
    
class Comentario(models.Model):
    valor = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    id_usuario_added = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    curtidas = models.IntegerField(default=0)

    def __str__(self):
        return self.valor
