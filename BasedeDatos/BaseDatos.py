# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    api_token = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Migrations(models.Model):
    migration = models.CharField(max_length=255)
    batch = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'migrations'


class ModeloCliente(models.Model):
    cliente_id = models.AutoField(primary_key=True)
    cedula = models.CharField(unique=True, max_length=10)
    nombres = models.CharField(max_length=70)
    apellidos = models.CharField(max_length=70)
    genero = models.CharField(max_length=30)
    estadocivil = models.CharField(db_column='estadoCivil', max_length=30)  # Field name made lowercase.
    correo = models.CharField(max_length=105)
    telefono = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    direccion = models.TextField()
    date_created = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'modelo_cliente'


class ModeloCuenta(models.Model):
    cuenta_id = models.AutoField(primary_key=True)
    numero = models.CharField(unique=True, max_length=20)
    fechaapertura = models.DateTimeField(db_column='fechaApertura')  # Field name made lowercase.
    tipocuenta = models.CharField(db_column='tipoCuenta', max_length=30)  # Field name made lowercase.
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.IntegerField()
    date_created = models.DateTimeField()
    updated_at = models.DateTimeField()
    cliente = models.ForeignKey(ModeloCliente, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'modelo_cuenta'


class ModeloTransaccion(models.Model):
    transaccion_id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField()
    tipo = models.CharField(max_length=30)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    date_created = models.DateTimeField()
    updated_at = models.DateTimeField()
    cuenta = models.ForeignKey(ModeloCuenta, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'modelo_transaccion'
