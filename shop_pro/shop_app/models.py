from django.db import models
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordernar = ('nome',)
        verbose_nome = 'categoria'
        verbose_nome_plural = 'categorias'

    def __str__(seflf):
        return self.name

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, realeted_name='produtos',on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    imagem = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado  models.DateTimefield(auto_now=True)

    class Meta:
        ordernar = ('name',)
        index_junto = (('id', 'slug'),)

    def __str_(self):
        return self.name

# Create your models here.
