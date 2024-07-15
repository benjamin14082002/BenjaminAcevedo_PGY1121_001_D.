from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import UsuarioForm, LoginForm, ReservaForm
from .models import Reserva, Medico, Horario
from django.contrib.auth.decorators import login_required
import json



def signup(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guarda el usuario en la base de datos
            login(request, user)  # Inicia sesión automáticamente después del registro
            if user.tipoUsuario == user.ADMIN:
                return redirect('administradores_view')
            else:
                return redirect('clientes_view')
    else:
        form = UsuarioForm()
    
    return render(request, 'login.html', {'form': form})

def main(request):
    return render(request, 'main.html')


def tienda(request):
    return render(request, 'agenda.html')


def signin(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_page')
    else:
        form = LoginForm()

    return render(request, 'signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('main_page')


def clientes_view(request):
    # Lógica específica para la vista de clientes/usuarios
    return render(request, 'clientes.html')


def administradores_view(request):
    # Lógica específica para la vista de administradores
    return render(request, 'admin.html')


@login_required
def agregar_al_carrito(request, reserva_id):
    reserva = Reserva.objects.get(id=reserva_id)
    carrito = request.session.get('carrito', {})
    
    if reserva_id not in carrito:
        if reserva.fecha.weekday() < 5:
            precio = 35000
        else:
            precio = 40000

        carrito[reserva_id] = {
            'medico': reserva.medico.nombre,
            'fecha': reserva.fecha.strftime("%Y-%m-%d"),
            'hora': reserva.horario.hora.strftime("%H:%M"),
            'precio': precio
        }

    request.session['carrito'] = carrito
    return redirect('ver_carrito')



@login_required
def checkout(request):
    carrito = request.session.get('carrito', {})
    if request.method == 'POST':
        # Aquí puedes procesar el pago y guardar las reservas
        for reserva_id in carrito:
            reserva = Reserva.objects.get(id=reserva_id)
            reserva.confirmada = True
            reserva.save()
        # Vaciar el carrito
        request.session['carrito'] = {}
        return redirect('confirmacion')
    return render(request, 'checkout.html', {'carrito': carrito, 'total': sum(item['precio'] for item in carrito.values())})

@login_required
def confirmacion(request):
    return render(request, 'confirmacion.html')

def ver_carrito(request):
    # Obtener las reservas guardadas en la cookie
    reservas_cookie = request.COOKIES.get('reservas')

    # Convertir el JSON de reservas a una lista de Python
    reservas = json.loads(reservas_cookie) if reservas_cookie else []

    context = {
        'reservas': reservas
    }
    return render(request, 'carrito.html', context)


