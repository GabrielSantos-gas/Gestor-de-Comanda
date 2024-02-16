from django.db import models

class Comanda(models.Model):
    nome = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data = models.DateField(auto_now_add=True)
    excluida = models.BooleanField(default=False)  # Adicione esta linha

    def __str__(self):
        return self.nome

    
    def delete(self, *args, **kwargs):
        self.nome = f"DELETED_{self.nome}"  # Prefixa o nome com "DELETED_" ao excluir
        self.save()
        super().delete(*args, **kwargs)


class Item(models.Model):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return f"{self.descricao} - R${self.valor}"
