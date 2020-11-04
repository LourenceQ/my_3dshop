from django.contrib import admin
from .models import Categoria, Produto

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome','slug']
    preopupulated_fields = {'slug':('name',)}

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome','slug','preco','disponivel','criado','atualizado']
    list_filter = ['disponivel','criado','atualizado']
    list_editable = ['preco','disponivel']
    preopopulated_fields = {'slug':('nome',)}
