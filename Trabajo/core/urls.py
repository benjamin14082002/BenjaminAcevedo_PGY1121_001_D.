from django.urls import path
from core import views 

urlpatterns = [
    path('login/', views.signup, name='login'),
    path('reservar/', views.tienda, name='agendar'),
    path('', views.main, name='main_page'),
    path('signin/', views.signin, name='signin'), 
    path('logout/', views.signout, name='signout'),
    path('clientes/', views.clientes_view, name='clientes'),
    path('administradores/', views.administradores_view, name='administradores'),
    path('agregar_al_carrito/<int:reserva_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
    
]

