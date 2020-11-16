from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop_app.models import Produto
from .cart import Carrinho
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

@require_POST
def carrinho_remove(request, produto_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho.remove(produto)
    return redirect('carrinho:carrinho_detalhe')

def carrinho_detalhe(request):
    carrinho = carrinho(request)
    return render(request,'carrinho/detalhe.html',{'carrinho':carrinho})
