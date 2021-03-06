from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    nome = models.CharField(max_length=200,db_index=True)
    slug = models.SlugField(max_length=200,unique=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:lista_produto_by_category',args=[self.slug])

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos',on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    imagem = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nome',)
        index_together = (('id', 'slug'),)

    def __str_(self):
        return self.name

    def get_absolute_url(selg):
        return reverse('shop:detalhe_produto',args=[self.id, self.slug])

# Create your models here.
