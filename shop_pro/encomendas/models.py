from django.db import models
from shop_app.models import Produto

# Create your models here.

class Encomenda(models. Model):
    primeiro_nome = models.CharField(max_length=50)
    ultimo_nome   = models.CharField(max_length=50)
    email         = models.EmailField()
    endereco      = models.CharField(max_length=250)
    cep           = models.CharField(max_length=20)
    cidade        = models.CharField(max_length=100)
    criado        = models.DateTimeField(auto_now_add=True)
    atualizado    = models.BooleanField(auto_now=True)
    pago          = models.BooleanField(default=False)

    class Meta:
        encomendando = ('-criado',)

    def __str__(self):
        return f'Encomenda {self.id}'

    def get_custo_total(self):
        return sum(item.get_custo() for item in self.items.all())

class EncomendarItem(models.Model):
    encomenda = models.ForeignKey(Encomenda,
                                  nome_relacionado='items',
                                  on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto,
                                nome_relacionado='encomendar_items',
                                on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_custo(self):
        return self.preco * self.quantidade
