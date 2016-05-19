from django.contrib import admin
from Stamping.models import *
from import_export.admin import ImportExportModelAdmin

class ColorAdmin(admin.ModelAdmin):
	list_display = ('nombre','referencia',)
	search_fields = ('nombre',)

class ComprainsumoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('cod_compra_insumo','cod_insumo','cod_persona','cantidad','valor')
	search_fields = ('cod_compra_insumo','cod_insumo','cod_persona','cantidad','valor')

class EstampadoAdmin(admin.ModelAdmin):
	list_display = ('cod_estampado','nombre',)
	search_fields = ('cod_estampado','nombre',)

class EstiloAdmin(admin.ModelAdmin):
	list_display = ('cod_estilo','nombre',)
	search_fields = ('cod_estilo','nombre',)

class InsumoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display = ('cod_insumo','nombre','referencia','tipo','fecha_compra','fecha_vencimiento')
	search_fields = ('cod_insumo','nombre','referencia','tipo','fecha_compra','fecha_vencimiento')

class InsumoproductoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display = ('cod_insumo_producto','cod_producto','cod_insumo','cantidad','valor',)
	search_fields = ('cod_insumo_producto','cod_producto','cod_insumo','cantidad','valor',)

class MarcaAdmin(admin.ModelAdmin):
	list_display = ('cod_marca','nombre',)
	search_fields = ('cod_marca','nombre',)

class PerfilAdmin(admin.ModelAdmin):
	list_display = ('cod_perfil','nombre')
	search_fields = ('cod_perfil','nombre')

class PersonaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display = ('cod_persona','cedula','nombre','apellido','fecha_nacimiento','telefono','movil','email')
	search_fields = ('cod_persona','cedula','nombre','apellido','fecha_nacimiento','telefono','movil','email')

class ProductoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display = ('nombre','valor_venta','valor_produccion','cantidad_existente','descripcion')
	search_fields = ('nombre','valor_venta','valor_produccion','cantidad_existente','descripcion')

class TallaAdmin(admin.ModelAdmin):
	list_display = ('cod_talla','numero','letra')

class TelaAdmin(admin.ModelAdmin):
	list_display = ('cod_tela','nombre','descripcion')

class VentaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display = ('cod_venta','cod_persona','fecha_movimiento')

class VentaproductoAdmin(ImportExportModelAdmin,admin.ModelAdmin):
	list_display = ('cod_venta_producto','cod_venta','cod_producto','valor')
	search_fields = ('cod_venta_producto','cod_venta','cod_producto','valor')

admin.site.register(Color,ColorAdmin)
admin.site.register(Comprainsumo,ComprainsumoAdmin)
admin.site.register(Estampado,EstampadoAdmin)
admin.site.register(Estilo,EstiloAdmin)
admin.site.register(Insumo,InsumoAdmin)
admin.site.register(Insumoproducto,InsumoproductoAdmin)
admin.site.register(Marca,MarcaAdmin)
admin.site.register(Perfil,PerfilAdmin)
admin.site.register(Persona,PersonaAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Talla,TallaAdmin)
admin.site.register(Tela,TelaAdmin)
admin.site.register(Venta,VentaAdmin)
admin.site.register(Ventaproducto,VentaproductoAdmin)
