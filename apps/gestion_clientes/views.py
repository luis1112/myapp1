from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from apps.modelo.models import Cliente, Cuenta
from .forms import FormularioCliente, FormularioCuenta
from django.db.models import Q

# Create your views here.
#index del gestion cliente
@login_required
def index(request):
    usuario=request.user
    if usuario.groups.filter(name="Gestion_Clientes").exists():
        listaClientes=Cliente.objects.all()
        busqueda = request.POST.get("busqueda")
        if busqueda:
            listaClientes = Cliente.objects.filter(
                Q(nombres__icontains = busqueda) | 
                Q(apellidos__icontains = busqueda) | 
                Q(cedula = busqueda)
            ).distinct()
        return render (request, 'clientes/index.html',locals())
    else:
        return render (request, 'login/forbiden.html',locals())

@login_required
def crearCliente(request):
    formulario_cliente=FormularioCliente(request.POST)
    formulario_cuenta=FormularioCuenta(request.POST)
    if request.method=='POST':
        if formulario_cliente.is_valid() and formulario_cuenta.is_valid():
            cliente = Cliente()
            datos_cliente = formulario_cliente.cleaned_data
            cliente.cedula = datos_cliente.get('cedula')
            cliente.nombres = datos_cliente.get('nombres')
            cliente.apellidos = datos_cliente.get('apellidos')
            cliente.genero = datos_cliente.get('genero')
            cliente.estadoCivil = datos_cliente.get('estadoCivil')
            cliente.correo = datos_cliente.get('correo')
            cliente.telefono = datos_cliente.get('telefono')
            cliente.celular = datos_cliente.get('celular')
            cliente.direccion = datos_cliente.get('direccion')
            #ORM
            cliente.save()
            cuenta = Cuenta()
            datos_cuenta = formulario_cuenta.cleaned_data
            cuenta.numero = datos_cuenta.get("numero")
            cuenta.saldo = datos_cuenta.get("saldo")
            cuenta.tipoCuenta = datos_cuenta.get("tipoCuenta")
            #ORM
            cuenta.save()
            user = User.objects.create_user(cliente.cedula, cliente.correo, cliente.cedula)
            user.first_name = cliente.nombres
            user.last_name = cliente.apellidos
            grupo = Group.objects.get(name= "clientes")
            user.groups.add(grupo)
            user.save()

            
        return redirect(index)
    return render(request, 'clientes/crear.html',locals())
def modificarCliente(request, cedula):
    if request.method=='POST':
        cliente=Cliente.objects.get(cedula=cedula)
        formulario_cliente=FormularioCliente(request.POST, instance=cliente)
        if formulario_cliente.is_valid():
            #ORM
            cliente.save()
            return redirect(index)
    cliente=Cliente.objects.get(cedula=cedula)
    formulario_cliente=FormularioCliente(instance=cliente)
    return render(request, 'clientes/modificar.html',locals())

def eliminarCliente(request, cedula):
    cliente=Cliente.objects.get(cedula=cedula)
    cliente.delete()
    return redirect(index)

def ListarCuentas(request, cedula):
    cliente=Cliente.objects.get(cedula=cedula)
    cuentas=Cuenta.objects.filter(cliente=cliente)
    return render(request, 'cuenta/index.html',locals())



def crearCuenta(request, cedula):
    formulario_cuenta=FormularioCuenta(request.POST)
    if request.method=='POST':
        if formulario_cuenta.is_valid() :
            cliente=Cliente.objects.get(cedula=cedula)
            #ORM
            cliente.save()
            cuenta = Cuenta()
            datos_cuenta = formulario_cuenta.cleaned_data
            cuenta.numero = datos_cuenta.get("numero")
            cuenta.saldo = datos_cuenta.get("saldo")
            cuenta.tipoCuenta = datos_cuenta.get("tipoCuenta")
            cuenta.cliente = cliente
            cuenta.save()
        return redirect(ListarCuentas, cliente.cedula)
    return render(request, 'cuenta/crear.html',locals())
def modificarCuenta(request):
    return render(request, 'hola principal')
def eliminarCuenta(request):
    return render(request, 'hola principal')

