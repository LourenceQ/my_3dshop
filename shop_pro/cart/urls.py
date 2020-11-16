from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('',views.carrinho_detalhe, name='carrinho_detalhe'),
    path('add/<int:produto_id>/',views.carrinho_adicionar, name='carrinho_adicionar'),
    path('remover/<int:produto_id>/',views.carrinho_remove, name='carrinho_remover'),
]
