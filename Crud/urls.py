
from django.urls import path
from .views import admin_mesas_alugadas, admin_mesas, alugar,aluguel_mesa_disponiveis, create_mesa, delete_mesas, index, create_empresa,create_cliente, lista_alugadas, logar_cliente, logar_empresa,logout_cliente,logout_empresa, update_mesas

urlpatterns = [

    path('', index,name='index'),
    path('cadastro_empresa/', create_empresa,name='create_empresa'),
    path('cadastro_cliente/', create_cliente,name='create_cliente'),
    path('cadastro_mesa/', create_mesa,name='create_mesa'),

    path('logout_cliente/', logout_cliente,name='logout_cliente'),
    path('logar_empresa/', logar_empresa,name='logar_empresa'),
    path('logout_empresa/', logout_empresa,name='logout_empresa'),
    path('logar_cliente/', logar_cliente,name='logar_cliente'),
    
    path('admin_mesas_alugadas/',admin_mesas_alugadas,name='admin_mesas_alugadas'),
    path('admin_mesas/',admin_mesas,name='admin_mesas'),
    path('aluguel_mesa_disponiveis/', aluguel_mesa_disponiveis,name='aluguel_mesa_disponiveis'),
    path('alugar/<int:mes_codigo>/', alugar,name='alugar'),
    path('lista_alugadas/', lista_alugadas,name='lista_alugadas'),
    
    path('deletar_mesas/<int:mes_codigo>/', delete_mesas,name='delete_mesas'),
    path('update_mesas/<int:mes_codigo>/', update_mesas,name='update_mesas'),

    

]
