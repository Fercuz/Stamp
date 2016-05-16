from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible 
class Color(models.Model):
    cod_color = models.AutoField(db_column='Cod_Color', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)
    referencia = models.CharField(db_column='Referencia', max_length=45, blank=True, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        # managed = False
        db_table = 'color'
        verbose_name = 'Color'
        verbose_name_plural = 'Colores'

class Comprainsumo(models.Model):
    cod_compra_insumo = models.AutoField(db_column='Cod_Compra_Insumo', primary_key=True)
    cod_insumo = models.ForeignKey('Insumo', models.DO_NOTHING, db_column='Cod_Insumo')
    cod_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='Cod_Persona')
    cantidad = models.CharField(db_column='Cantidad', max_length=45)
    valor = models.FloatField(db_column='Valor')

    def __str__(self):
        return self.cod_compra_insumo

    class Meta:
        managed = False
        db_table = 'comprainsumo'
        verbose_name = 'Compra de Insumo'
        verbose_name_plural = 'Compra de Insumos'

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

@python_2_unicode_compatible 
class Estampado(models.Model):
    cod_estampado = models.AutoField(db_column='Cod_Estampado', primary_key=True)  
    nombre = models.CharField(db_column='Nombre', max_length=45)  
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True, null=True) 

    def __str__(self):
            return self.nombre

    class Meta:
        managed = False
        db_table = 'estampado'
        verbose_name = 'Estampado'
        verbose_name_plural = 'Estampados'

@python_2_unicode_compatible 
class Estilo(models.Model):
    cod_estilo = models.AutoField(db_column='Cod_Estilo', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45)

    def __str__(self):
        return self.nombre

    class Meta:
        # managed = False
        db_table = 'estilo'
        verbose_name = 'Estilo'
        verbose_name_plural = 'Estilos'

@python_2_unicode_compatible 
class Insumo(models.Model):
    cod_insumo = models.AutoField(db_column='Cod_Insumo', primary_key=True)  
    nombre = models.CharField(db_column='Nombre', max_length=45)  
    referencia = models.CharField(db_column='Referencia', max_length=45)  
    tipo = models.CharField(db_column='Tipo', max_length=45)  
    fecha_compra = models.DateField(db_column='Fecha_Compra')  
    fecha_vencimiento = models.DateField(db_column='Fecha_Vencimiento')  

    def __str__(self):
        return self.nombre

    class Meta:
        # managed = False
        db_table = 'insumo'
        verbose_name = 'Insumo'
        verbose_name_plural = 'Insumos'

@python_2_unicode_compatible 
class Insumoproducto(models.Model):
    cod_insumo_producto = models.AutoField(db_column='Cod_Insumo_Producto', primary_key=True)  
    cod_producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='Cod_Producto')  
    cod_insumo = models.ForeignKey(Insumo, models.DO_NOTHING, db_column='Cod_Insumo')  
    cantidad = models.CharField(db_column='Cantidad', max_length=45)  
    valor = models.FloatField(db_column='Valor')  

    def __str__(self):
        return self.Cod_Insumo_Producto

    class Meta:
        # managed = False
        db_table = 'insumoproducto'
        verbose_name = 'Insumo Producto'
        verbose_name_plural = 'Insumo de Productos'

@python_2_unicode_compatible 
class Marca(models.Model):
    cod_marca = models.AutoField(db_column='Cod_Marca', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45)

    def __str__(self):
        return self.nombre

    class Meta:
        # managed = False
        db_table = 'marca'
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

@python_2_unicode_compatible 
class Perfil(models.Model):
    cod_perfil = models.AutoField(db_column='Cod_Perfil', primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45)

    def __str__(self):
        return self.nombre

    class Meta:
        # managed = False
        db_table = 'perfil'
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'

@python_2_unicode_compatible 
class Persona(models.Model):
    cod_persona = models.AutoField(db_column='Cod_Persona', primary_key=True)  
    cod_perfil = models.ForeignKey(Perfil, models.DO_NOTHING, db_column='Cod_Perfil')  
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
        # managed = False
        db_table = 'persona'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

@python_2_unicode_compatible 
class Producto(models.Model):
    cod_producto = models.AutoField(db_column='Cod_Producto', primary_key=True)  
    cod_estampado = models.ForeignKey(Estampado, models.DO_NOTHING, db_column='Cod_Estampado')  
    cod_tela = models.ForeignKey('Tela', models.DO_NOTHING, db_column='Cod_Tela')  
    cod_marca = models.ForeignKey(Marca, models.DO_NOTHING, db_column='Cod_Marca')  
    cod_talla = models.ForeignKey('Talla', models.DO_NOTHING, db_column='Cod_Talla')  
    cod_color = models.ForeignKey(Color, models.DO_NOTHING, db_column='Cod_Color')  
    cod_estilo = models.ForeignKey(Estilo, models.DO_NOTHING, db_column='Cod_Estilo')  
    nombre = models.CharField(db_column='Nombre', max_length=45)  
    valor_venta = models.IntegerField(db_column='Valor_Venta')  
    valor_produccion = models.IntegerField(db_column='Valor_Produccion')  
    cantidad_existente = models.IntegerField(db_column='Cantidad_Existente')  
    stock_minimo = models.IntegerField(db_column='Stock_Minimo')  
    stock_maximo = models.IntegerField(db_column='Stock_Maximo')  
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True, null=True) 

    def __str__(self):
        return self.nombre

    class Meta:
        # managed = False
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

@python_2_unicode_compatible 
class Talla(models.Model):
    cod_talla = models.AutoField(db_column='Cod_Talla', primary_key=True)
    numero = models.CharField(db_column='Numero', max_length=45, blank=True, null=True)
    letra = models.CharField(db_column='Letra', max_length=45, blank=True, null=True)

    def __str__(self):
        return self.letra

    class Meta:
        # managed = False
        db_table = 'talla'
        verbose_name = 'Talla'
        verbose_name_plural = 'Tallas'

@python_2_unicode_compatible 
class Tela(models.Model):
    cod_tela = models.AutoField(db_column='Cod_Tela', primary_key=True)  
    nombre = models.CharField(db_column='Nombre', max_length=45)  
    descripcion = models.CharField(db_column='Descripcion', max_length=45, blank=True, null=True)  
    
    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'tela'
        verbose_name = 'Tela'
        verbose_name_plural = 'Telas'

@python_2_unicode_compatible 
class Venta(models.Model):
    cod_venta = models.AutoField(db_column='Cod_Venta', primary_key=True)  
    cod_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='Cod_Persona')  
    fecha_movimiento = models.DateField(db_column='Fecha_Movimiento')  
    monto = models.FloatField(db_column='Monto')  

    def __str__(self):
        return self.cod_venta

    class Meta:
        managed = False
        db_table = 'venta'
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'

@python_2_unicode_compatible 
class Ventaproducto(models.Model):
    cod_venta_producto = models.AutoField(db_column='Cod_Venta_Producto', primary_key=True)  
    cod_venta = models.ForeignKey(Venta, models.DO_NOTHING, db_column='Cod_Venta')  
    cod_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='Cod_Producto')  
    cantidad = models.CharField(db_column='Cantidad', max_length=45)  
    valor = models.FloatField(db_column='Valor')  

    def __str__(self):
        return self.cod_venta_producto

    class Meta:
        managed = False
        db_table = 'ventaproducto'
        verbose_name = 'Venta de Producto'
        verbose_name_plural = 'Ventas de Productos'
