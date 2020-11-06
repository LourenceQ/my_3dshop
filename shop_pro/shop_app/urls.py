from django.urls import path
from .import views

app_name = "shop_app"

urlpatterns = [
    path('',views.lista_produtos, name ='product_list'),
    path('<slug:category_slug>/',views.lista_produtos,name='lista_produtos_by_category'),
    path('<int:id>/<slug:slug>/',views.detalhe_produto,name='detalhe_produto'),
]
