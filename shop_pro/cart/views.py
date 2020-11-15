from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import AdicionaProdutoCarrinhoForm

# Create your views here.

@requirea_POST
def cart_add(request, product_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)
    form = AdicionaProdutoCarrinhoForm(request.POST)
    if form.is_valid():
        cd = form.claned_data
        carrinho.add(produto=produto,
                     quantidade=cd['quantidade'],
                     override_quantidade=cd['override'])
    return redirect('carrinho:carrinho_detalhe')
