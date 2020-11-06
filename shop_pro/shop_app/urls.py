from django.urls import path
from .import views

app_name = "shop_app"

urlpatterns = [
    path('',views.lista_produto, name ='produto_lista'),
    path('<slug:category_slug>/',views.lista_produto,name='lista_produto_by_category'),
    path('<int:id>/<slug:slug>/',views.detalhe_produto,name='detalhe_produto'),
]
