from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Cliente(models.Model):
    codigo_cliente = models.AutoField(db_column='Codigo_Cliente', primary_key=True, verbose_name=u"Codigo")  
    cedula = models.CharField(db_column='Cedula', max_length=45)  
    nombre = models.CharField(db_column='Nombre', max_length=45)  
    apellido = models.CharField(db_column='Apellido', max_length=45)  
    fecha_nacimiento = models.DateField(db_column='Fecha_Nacimiento')  
    telefono = models.CharField(db_column='Telefono', max_length=45)  
    direccion = models.CharField(db_column='Direccion', max_length=45)  
    movil = models.CharField(db_column='Movil', max_length=45, blank=True, null=True)  
    email = models.CharField(db_column='Email', max_length=45)  

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


@python_2_unicode_compatible
class Color(models.Model):
    codigo_color = models.AutoField(db_column='Codigo_Color', primary_key=True)  
    nombre = models.CharField(db_column='Nombre', max_length=45)  
    referencia = models.CharField(db_column='Referencia', max_length=45, blank=True,
                                  null=True)  

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'color'
        verbose_name = 'Color'
        verbose_name_plural = 'Colores'


@python_2_unicode_compatible
class Compra(models.Model):
    codigo_compra = models.AutoField(db_column='Codigo_Compra', primary_key=True)  
    codigo_insumo = models.ForeignKey('Insumo', models.DO_NOTHING,
                                      db_column='Codigo_Insumo',verbose_name=u'Insumo')
    codigo_empleado = models.ForeignKey('Empleado', models.DO_NOTHING,
                                        db_column='Codigo_Empleado',verbose_name=u'Empleado')
    cantidad = models.CharField(db_column='Cantidad', max_length=45)  
    precio = models.FloatField(db_column='Precio')  
    fecha = models.DateField(db_column='Fecha')  

    def __str__(self):
        return self.codigo_compra

    class Meta:
        managed = False
        db_table = 'compra'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


@python_2_unicode_compatible
class Detalle(models.Model):
    codigo_detalle = models.AutoField(db_column='Codigo_Detalle', primary_key=True)  
    codigo_producto = models.ForeignKey('Producto', models.DO_NOTHING,
                                        db_column='Codigo_Producto')  
    codigo_insumo = models.ForeignKey('Insumo', models.DO_NOTHING,
                                      db_column='Codigo_Insumo')  
    descripcion = models.CharField(db_column='Descripcion', max_length=45)  
    referencia = models.CharField(db_column='Referencia', max_length=45)  

    def __str__(self):
        return self.descripcion

    class Meta:
        managed = False
        db_table = 'detalle'
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'


@python_2_unicode_compatible
class Empleado(models.Model):
    codigo_empleado = models.AutoField(db_column='Codigo_Empleado', primary_key=True)  
    cedula = models.CharField(db_column='Cedula', max_length=45)  
    nombre = models.CharField(db_column='Nombre', max_length=45)  
    apellido = models.CharField(db_column='Apellido', max_length=45)  
    fecha_nacimiento = models.DateField(db_column='Fecha_Nacimiento')  
    fecha_contratacion = models.DateField(db_column='Fecha_Contratacion')  
    telefono = models.CharField(db_column='Telefono', max_length=45)  
    direccion = models.CharField(db_column='Direccion', max_length=45)  
    movil = models.CharField(db_column='Movil', max_length=45, blank=True, null=True)  
    email = models.CharField(db_column='Email', max_length=45)  

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'


@python_2_unicode_compatible
class Estampado(models.Model):
    codigo_estampado = models.AutoField(db_column='Codigo_Estampado', primary_key=True)  
    nombre = models.CharField(db_column='Nombre', max_length=45)  
    imagen = models.CharField(db_column='Imagen', max_length=45, blank=True, null=True)  
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True,
                                   null=True)  

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'estampado'
        verbose_name = 'Estampado'
        verbose_name_plural = 'Estampados'


@python_2_unicode_compatible
class Estilo(models.Model):
    codigo_estilo = models.AutoField(db_column='Codigo_Estilo', primary_key=True)  
    nombre = models.CharField(db_column='Nombre', max_length=45)  

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'estilo'
        verbose_name = 'Estilo'
        verbose_name_plural = 'Estilos'


@python_2_unicode_compatible
class Factura(models.Model):
    codigo_factura = models.AutoField(db_column='Codigo_Factura', primary_key=True,)
    codigo_cliente = models.ForeignKey(Cliente, models.DO_NOTHING,
                                       db_column='Codigo_Cliente',verbose_name=u"Cliente")
    codigo_empleado = models.ForeignKey(Empleado, models.DO_NOTHING,
                                        db_column='Codigo_Empleado',verbose_name=u"Empleado")
    fecha = models.DateField(db_column='Fecha')  
    total = models.FloatField(db_column='Total')  

    def __str__(self):
        return self.codigo_factura

    class Meta:
        managed = False
        db_table = 'factura'
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'


@python_2_unicode_compatible
class Insumo(models.Model):
    codigo_insumo = models.AutoField(db_column='Codigo_Insumo', primary_key=True)  
    nombre = models.CharField(db_column='Nombre', max_length=45)  
    referencia = models.CharField(db_column='Referencia', max_length=45)  
    tipo = models.CharField(db_column='Tipo', max_length=45)  
    fecha_compra = models.DateField(db_column='Fecha_Compra')  
    fecha_vencimiento = models.DateField(db_column='Fecha_Vencimiento')  

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'insumo'
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'


@python_2_unicode_compatible
class Producto(models.Model):
    codigo_producto = models.AutoField(db_column='Codigo_Producto', primary_key=True)  
    codigo_tela = models.ForeignKey('Tela', models.DO_NOTHING, db_column='Codigo_Tela',verbose_name=u'Tela')
    codigo_estilo = models.ForeignKey(Estilo, models.DO_NOTHING,
                                      db_column='Codigo_Estilo',verbose_name=u'Estilo')
    codigo_talla = models.ForeignKey('Talla', models.DO_NOTHING, db_column='Codigo_Talla',verbose_name=u'Talla')
    codigo_color = models.ForeignKey(Color, models.DO_NOTHING, db_column='Codigo_Color',verbose_name=u'Color')
    codigo_estampado = models.ForeignKey(Estampado, models.DO_NOTHING,
                                         db_column='Codigo_Estampado',verbose_name=u'Estampado')
    nombre = models.CharField(db_column='Nombre', max_length=45)  
    precio = models.IntegerField(db_column='Precio')  
    stock = models.IntegerField(db_column='Stock')  
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True,
                                   null=True)  

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


@python_2_unicode_compatible
class Talla(models.Model):
    codigo_talla = models.AutoField(db_column='Codigo_Talla', primary_key=True)  
    numero = models.CharField(db_column='Numero', max_length=45)  
    letra = models.CharField(db_column='Letra', max_length=45, blank=True, null=True)  

    def __str__(self):
        return self.letra

    class Meta:
        managed = False
        db_table = 'talla'
        verbose_name = 'Talla'
        verbose_name_plural = 'Tallas'


@python_2_unicode_compatible
class Tela(models.Model):
    codigo_tela = models.AutoField(db_column='Codigo_Tela', primary_key=True)  
    nombre = models.CharField(db_column='Nombre', max_length=45)  
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True,
                                   null=True)  

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'tela'
        verbose_name = 'Tela'
        verbose_name_plural = 'Telas'


@python_2_unicode_compatible
class Venta(models.Model):
    codigo_venta = models.AutoField(db_column='Codigo_Venta', primary_key=True)  
    codigo_factura = models.ForeignKey(Factura, models.DO_NOTHING,
                                       db_column='Codigo_Factura')  
    codigo_producto = models.ForeignKey(Producto, models.DO_NOTHING,
                                        db_column='Codigo_Producto')  
    cantidad = models.FloatField(db_column='Cantidad', max_length=45)
    precio = models.FloatField(db_column='Precio')  

    def __str__(self):
        return self.codigo_venta

    class Meta:
        managed = False
        db_table = 'venta'
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

@python_2_unicode_compatible 
class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'django_migrations'
