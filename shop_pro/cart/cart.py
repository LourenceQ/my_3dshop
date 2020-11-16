from decimal import Decimal
from django.conf import settings
from shop_app.models import Produto

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

    def remove(self, product):
        """
        Remove o produto do carrinho.
        """
        produto_id = str(produto.id)
        if produto_id in self.cart:
            del self.carrinho[produto_id]
            self.save()

    def __iter__(self):
        """
        Itera sobre os items no carrinho e pega os produtos do banco de dados.
        """
        produto_ids = self.carrinho.keys()
        # pega o produto dos objetos e adiciona-os ao carrinho
        produtos = Produto.objects.filter(id__in=produto_ids)

        carrinho = self.carrinho.copy()
        for produto in produtos:
            carrinho[str(produto.id)]['produto'] = produto

        for item in carrinho.values():
            item['preco'] = Decimal(item['preco'])
            item['total_preco'] = item['preco'] * item['quantidade']
            yield item

        def __len__(self):
            """
            Counta todos os items no carrinho.
            """
            return sum(item['quantidade'] for item in self.carrinho.valor())
