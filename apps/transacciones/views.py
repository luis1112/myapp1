from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.db.models import Q
from apps.modelo.models import Cliente, Cuenta, Transaccion
from .forms import FormularioTransaccion


# Create your views here.

def index(request):
    usuario=request.user
    if usuario.groups.filter(name="transacciones").exists():
        listaCuentas=Cuenta.objects.all()
        return render (request, 'cuenta/index_transacciones.html',locals())
    else:
        return render (request, 'login/forbiden.html',locals())

def getCuentaPorCliente(request, numero):
    usuario=request.user
    if usuario.groups.filter(name="transacciones").exists():
        cuenta=Cuenta.objects.get(numero=numero)
        if cuenta:
            cliente=Cliente.objects.get(cedula=cuenta.cliente)
        return render (request, 'transacciones/cuenta_cliente.html',locals())
    else:
        return render (request, 'login/forbiden.html',locals())
    listaClientes=Cliente.objects.all()
    return render (request, '/'. locals())

def depositar(request, numero):
    usuario=request.user
    if usuario.groups.filter(name="transacciones").exists():
        formulario=FormularioTransaccion(request.POST)
        cuenta=Cuenta.objects.get(numero=numero)
        if request.method == 'POST':
            transaccion = Transaccion()
            transaccion.tipo = 'deposito'
            transaccion.valor = float(request.POST.get('valor'))
            transaccion.descripcion = request.POST.get('descripcion')
            transaccion.cuenta = cuenta
            transaccion.save()
            valorTotal = float(request.POST.get('valor')) +float (cuenta.saldo)
            cuenta.saldo = valorTotal
            cuenta.save()
            return redirect(index)
        return render (request, 'transacciones/depositar.html',locals())
    else:
        return render (request, 'login/forbiden.html',locals())
    listaClientes=Cliente.objects.all()
    return render (request, '/'. locals())