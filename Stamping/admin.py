from django.contrib import admin
from Stamping.models import *
from import_export.admin import ImportExportModelAdmin
from Stamping.forms import Venta_Form


class ClienteAdmin(admin.ModelAdmin):
	list_display = ('cedula','nombre','apellido','fecha_nacimiento','telefono','movil','email')
	search_fields = ('cedula','nombre','apellido','fecha_nacimiento','telefono','movil','email')

class ColorAdmin(admin.ModelAdmin):
	list_display = ('nombre','referencia',)
	search_fields = ('nombre',)

class CompraAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('codigo_compra','comprador','fecha')
	search_fields  = ('codigo_compra','comprador','fecha')

class DetallecompraAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('codigo_insumo','codigo_compra','cantidad','precio')
	search_fields = ('codigo_insumo','codigo_compra','cantidad','precio')

class DetalleinsumoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('codigo_producto','codigo_insumo','descripcion')
	search_fields = ('codigo_producto','codigo_insumo','descripcion')

class DetalleventaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('codigo_detalle_venta','codigo_producto','cantidad','precio')
	search_fields = ('codigo_detalle_venta','codigo_producto','cantidad','precio')

class EstampadoAdmin(admin.ModelAdmin):
	list_display = ('codigo_estampado','nombre','imagen','descripcion')
	search_fields = ('codigo_estampado','nombre',)

class EstiloAdmin(admin.ModelAdmin):
	list_display = ('codigo_estilo','nombre',)
	search_fields = ('codigo_estilo','nombre',)

class InsumoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display = ('codigo_insumo','nombre','referencia','tipo','fecha_compra','fecha_vencimiento')
	search_fields = ('codigo_insumo','nombre','referencia','tipo','fecha_compra','fecha_vencimiento')

class ProductoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display = ('nombre','precio','stock','descripcion')
	search_fields = ('nombre','precio','stock','descripcion')

class TallaAdmin(admin.ModelAdmin):
	list_display = ('codigo_talla','numero','letra')

class TelaAdmin(admin.ModelAdmin):
	list_display = ('codigo_tela','nombre','descripcion')

class OpcionAdmin(admin.TabularInline):
	model = Detalleventa
	extra = 1

class VentaAdmin(ImportExportModelAdmin,admin.ModelAdmin):

	model = Venta
	form = Venta_Form
	list_display = ('codigo_venta','codigo_cliente','vendedor','fecha')
	#readonly_fields = ('vendedor','fecha')

	fielsets = [
				('Producto',{'fields':['codigo_producto']}),
				(None,{'fields':['cantidad']}),
				(None, {'fields': ['precio']}),
	]
	inlines = [OpcionAdmin]

admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Color,ColorAdmin)
#admin.site.register(Compra,CompraAdmin)
#admin.site.register(Detallecompra,DetallecompraAdmin)
#admin.site.register(Detalleinsumo,DetalleinsumoAdmin)
#admin.site.register(Detalleventa,DetalleventaAdmin)
admin.site.register(Estampado,EstampadoAdmin)
admin.site.register(Estilo,EstiloAdmin)
admin.site.register(Insumo,InsumoAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Talla,TallaAdmin)
admin.site.register(Tela,TelaAdmin)
admin.site.register(Venta,VentaAdmin)




