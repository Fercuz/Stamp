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

    def __unicode__(self):
        return u'%i' % self.nombre

    class Meta:
        managed = False
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


@python_2_unicode_compatible
class Color(models.Model):
    codigo_color = models.AutoField(db_column='Codigo_Color', primary_key=True, verbose_name=u"Codigo")  
    nombre = models.CharField(db_column='Nombre', max_length=45)  
    referencia = models.CharField(db_column='Referencia', max_length=45, blank=True,
                                  null=True)  

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%i' % self.nombre


    class Meta:
        managed = False
        db_table = 'color'
        verbose_name = 'Color'
        verbose_name_plural = 'Colores'


@python_2_unicode_compatible
class Compra(models.Model):
    codigo_compra = models.AutoField(db_column='Codigo_Compra', primary_key=True)  
    comprador = models.CharField(db_column='Comprador', max_length=45)  
    fecha = models.DateField(db_column='Fecha')  

    def __str__(self):
        return self.codigo_compra

    def __unicode__(self):
        return u'%i' % self.codigo_compra

    class Meta:
        managed = False
        db_table = 'compra'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


@python_2_unicode_compatible
class Detallecompra(models.Model):
    codigo_detalle_compra = models.AutoField(db_column='Codigo_Detalle_Compra',primary_key=True)
    codigo_compra = models.ForeignKey(Compra, models.DO_NOTHING, db_column='Codigo_Compra')  
    codigo_insumo = models.ForeignKey('Insumo', models.DO_NOTHING, db_column='Codigo_Insumo')  
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=10, decimal_places=0)  
    precio = models.FloatField(db_column='Precio', blank=True, null=True)  

    def __str__(self):
        return self.codigo_insumo

    def __unicode__(self):
        return u'%i' % self.codigo_insumo

    class Meta:
        managed = False
        db_table = 'detallecompra'
        unique_together = (('codigo_detalle_compra', 'codigo_compra'),)
        verbose_name = 'Detalle Compra'
        verbose_name_plural = 'Detalles de Compras'

@python_2_unicode_compatible
class Detalleinsumo(models.Model):
    codigo_detalle_insumo = models.AutoField(db_column='Codigo_Detalle_Insumo',primary_key=True)
    codigo_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Codigo_Producto')
    codigo_insumo = models.ForeignKey('Insumo', models.DO_NOTHING, db_column='Codigo_Insumo')  
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True, null=True)  

    def __str__(self):
        return self.descripcion

    def __unicode__(self):
        return u'%i' % self.descripcion

    class Meta:
        managed = False
        db_table = 'detalleinsumo'
        verbose_name = 'Detalle Insumo'
        verbose_name_plural = 'Detalle de Insumos'

@python_2_unicode_compatible
class Detalleventa(models.Model):
    codigo_detalle_venta = models.AutoField(db_column='Codigo_Detalle_Venta',primary_key=True)
    codigo_venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='Codigo_Venta') 
    codigo_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Codigo_Producto') 
    cantidad = models.DecimalField(db_column='Cantidad', max_digits=10, decimal_places=0) 
    precio = models.FloatField(db_column='Precio', blank=True, null=True) 

    def __str__(self):
        return self.codigo_detalle_venta

    def __unicode__(self):
        return u'%i' % self.codigo_detalle_venta

    class Meta:
        managed = False
        db_table = 'detalleventa'
        unique_together = (('codigo_detalle_venta', 'codigo_venta'),)
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalle de Ventas'

@python_2_unicode_compatible
class Estampado(models.Model):
    codigo_estampado = models.AutoField(db_column='Codigo_Estampado', primary_key=True)  
    nombre = models.CharField(db_column='Nombre', max_length=45)  
    imagen = models.CharField(db_column='Imagen', max_length=45, blank=True, null=True)  
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True,
                                   null=True)  

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return u'%i' % self.nombre

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

    def __unicode__(self):
        return u'%i' % self.nombre

    class Meta:
        managed = False
        db_table = 'estilo'
        verbose_name = 'Estilo'
        verbose_name_plural = 'Estilos'

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

    def __unicode__(self):
        return u'%i' % self.nombre

    class Meta:
        managed = False
        db_table = 'insumo'
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'


@python_2_unicode_compatible
class Producto(models.Model):
    codigo_producto = models.AutoField(db_column='Codigo_Producto', primary_key=True)
    codigo_tela = models.ForeignKey('Tela', models.DO_NOTHING, db_column='Codigo_Tela',verbose_name=u'Tela')
    codigo_estilo = models.ForeignKey(Estilo, models.DO_NOTHING,db_column='Codigo_Estilo',verbose_name=u'Estilo')
    codigo_talla = models.ForeignKey('Talla', models.DO_NOTHING, db_column='Codigo_Talla',verbose_name=u'Talla')
    codigo_color = models.ForeignKey(Color, models.DO_NOTHING, db_column='Codigo_Color',verbose_name=u'Color')
    codigo_estampado = models.ForeignKey(Estampado, models.DO_NOTHING, db_column='Codigo_Estampado',verbose_name=u'Estampado')
    nombre = models.CharField(db_column='Nombre', max_length=45)  
    precio = models.FloatField(db_column='Precio')  
    stock = models.DecimalField(db_column='Stock', max_digits=3, decimal_places=0)  
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True,
                                   null=True)  

    def __str__(self):
        return self.nombre


    def __unicode__(self):
        return u'%i' % self.nombre

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

    def __unicode__(self):
        return u'%i' % self.letra

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
    
    def __unicode__(self):
        return u'%i' % self.nombre

    class Meta:
        managed = False
        db_table = 'tela'
        verbose_name = 'Tela'
        verbose_name_plural = 'Telas'


@python_2_unicode_compatible
class Venta(models.Model):
    codigo_venta = models.AutoField(db_column='Codigo_Venta', primary_key=True)
    codigo_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='Codigo_Cliente',verbose_name=u'Cliente')
    vendedor = models.CharField(db_column='Vendedor', max_length=45)  
    fecha = models.DateField(db_column='Fecha',auto_now_add=True)

    @property
    def Venta_Total(self):
        return self.cantidad*self.precio

    total = property(Venta_Total)

    def __str__(self):
        return self.codigo_venta

    def __unicode__(self):
        return u'%i' % self.codigo_venta

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
