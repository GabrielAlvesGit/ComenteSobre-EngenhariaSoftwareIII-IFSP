from django.db import models

class Topico(models.Model):
    """Um assunto sobre o qual o usuário está interessado em comentar"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    id_usuario_added = models.IntegerField()

    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.name