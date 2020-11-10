from django.urls import path
from .import views

app_name = "shop_app"

urlpatterns = [
    path('',views.lista_produto, name ='lista_produto'),
    path('<slug:categoria_slug>/',views.lista_produto,name='lista_produto_by_categoria'),
    path('<int:id>/<slug:slug>/',views.detalhe_produto,name='detalhe_produto'),
]
