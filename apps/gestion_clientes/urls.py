from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="clientes"),
    path('crear_Clientes',views.crearCliente, name="crear_clientes"),
    path('modificar_Clientes/<int:cedula>/',views.modificarCliente, name="modificar_Clientes"),
    path('cuentas/<int:cedula>/',views.ListarCuentas, name="cuentas"),
    path('crear_cuentas/<int:cedula>/',views.crearCuenta, name="crear_cuentas"),
    path('eliminar_Clientes/<int:cedula>/',views.eliminarCliente, name="eliminar_Clientes"),
]