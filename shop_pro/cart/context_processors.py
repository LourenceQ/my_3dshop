from .cart import Carrinho

def cart(request):
    return {'cart':Carrinho(request)}
