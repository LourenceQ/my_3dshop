from decimal import Decimal
from django.conf import settings
from shop.models import Produto

class Carrinho(object):
    def __init__(self, request):
        """
        Inicia o carrinho.
        """
        self.session = request.session
        carrinho = self.session.get(settings.CARRINHO_SESSION_ID)
        if not carrinho:
            # salva um carrinho vazio na sessão
            carrinho = self.session[settings.CART_SESSION_ID]= {}
        self.carrinho = cart

    def adiciona(self, produto, quantidade=1, override_quantidade=False):
        """
        adiciona o produto par ao carrinho ow atualiza a quantidade.
        """
        produto_id = str(produto.id)
        if produto_id not in self.carrinho:
            self.carrinho[produto_id] = {'quantidade': 0,
                                         'preco': str(produto.preco)}
        if override_quantidade:
            self.carrinho[produto_id]['quantidade']=quantidade
        else:
            self.cart[produto_id]['quantidade'] += quantidade
        self.save()
    def save(self):
        # marca a sessão como modificada para certificar que foi salva
        self.session.modified = True
