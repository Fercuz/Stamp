from django.contrib import admin
from Stamping.models import *
from import_export.admin import ImportExportModelAdmin

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('cedula','nombre','apellido','fecha_nacimiento','telefono','movil','email')
	search_fields = ('cedula','nombre','apellido','fecha_nacimiento','telefono','movil','email')

class ColorAdmin(admin.ModelAdmin):
	list_display = ('nombre','referencia',)
	search_fields = ('nombre',)

class CompraAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('codigo_compra','codigo_insumo','codigo_empleado','cantidad','precio','fecha')
	search_fields = ('codigo_compra','codigo_insumo','codigo_empleado','cantidad','precio','fecha')

class DetalleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('codigo_detalle','codigo_producto','codigo_insumo','descripcion')
	search_fields = ('codigo_detalle','codigo_producto','codigo_insumo','descripcion')

class EmpleadoAdmin(admin.ModelAdmin):
	list_display = ('cedula','nombre','apellido','fecha_nacimiento','fecha_contratacion','telefono','movil','email')
	search_fields = ('cedula','nombre','apellido','fecha_nacimiento','fecha_contratacion','telefono','movil','email')

class EstampadoAdmin(admin.ModelAdmin):
	list_display = ('codigo_estampado','nombre',)
	search_fields = ('codigo_estampado','nombre',)

class EstiloAdmin(admin.ModelAdmin):
	list_display = ('codigo_estilo','nombre',)
	search_fields = ('codigo_estilo','nombre',)

class FacturaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	readonly_fields = ('codigo_factura','codigo_cliente','codigo_empleado','fecha','total')
	#search_fields = ('codigo_factura','codigo_cliente','codigo_empleado','fecha','total')

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

class VentaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display = ('codigo_venta','codigo_factura','codigo_producto','cantidad','precio')


admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(Compra,CompraAdmin)
admin.site.register(Detalle,DetalleAdmin)
admin.site.register(Empleado,EmpleadoAdmin)
admin.site.register(Estampado,EstampadoAdmin)
admin.site.register(Estilo,EstiloAdmin)
admin.site.register(Factura,FacturaAdmin)
admin.site.register(Insumo,InsumoAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Talla,TallaAdmin)
admin.site.register(Tela,TelaAdmin)
admin.site.register(Venta,VentaAdmin)

 