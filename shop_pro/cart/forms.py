from django import forms

ESCOLHA_QUANTIDADE_PRODUTOS = [(i, str(i)) for i in range(1, 21)]

class AdicionaProdutoCarrinhoForm(forms.Form):
    quantidade = forms.TyedChoiceField(
                                escolhas= ESCOLHA_QUANTIDADE_PRODUTOS,
                                coerce=int)
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)
