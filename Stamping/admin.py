from django.contrib import admin
from models import *

class ColorAdmin(admin.ModelAdmin):
	list_display = ('nombre','referencia')
	search_fields = ('nombre',)

class EstiloAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	search_fields = ('nombre',)

class InsumoAdmin(admin.ModelAdmin):
	list_display = ('nombre','referencia','tipo','fecha_vencimiento')
	search_fields = ('nombre','referencia','tipo')

class InsumoproductoAdmin(admin.ModelAdmin):
	list_display = ('cantidad','valor')
	search_fields = ('valor',)

class MarcaAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	search_fields = ('nombre',)

class MovimientoAdmin(admin.ModelAdmin):
	list_display = ('fecha_movimiento','monto')
	search_fields = ('fecha_movimiento','monto')

class MovimientoinsumoAdmin(admin.ModelAdmin):
	list_display = ('cantidad','valor')
	search_fields = ('valor',)

class MovimientoproductoAdmin(admin.ModelAdmin):
	list_display = ('cantidad','valor')
	search_fields = ('valor',)

class PerfilAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

class PersonaAdmin(admin.ModelAdmin):
	list_display = ('cedula','nombre','apellido','fecha_nacimiento','telefono','movil','email')
	search_fields = ('cedula','nombre','apellido','fecha_nacimiento','telefono','movil','email')
	actions = [export_as_csv]

class ProductoAdmin(admin.ModelAdmin):
	list_display = ('nombre','valor_venta','valor_produccion','cantidad_existente','descripcion')
	search_fields = ('nombre','valor_venta','valor_produccion','cantidad_existente','descripcion')

class TallaAdmin(admin.ModelAdmin):
	list_display = ('numero','letra')

class TipoestampadoAdmin(admin.ModelAdmin):
	list_display = ('nombre','descripcion')

class TipomovimientoAdmin(admin.ModelAdmin):
	list_display = ('nombre',)

class TipotelaAdmin(admin.ModelAdmin):
	list_display = ('nombre',)
	search_fields = ('nombre',)

admin.site.register(Color,ColorAdmin)
admin.site.register(Estilo,EstiloAdmin)
admin.site.register(Insumo,InsumoAdmin)
admin.site.register(Insumoproducto,InsumoproductoAdmin)
admin.site.register(Marca,MarcaAdmin)
admin.site.register(Movimiento,MovimientoAdmin)
admin.site.register(Movimientoinsumo,MovimientoinsumoAdmin)
admin.site.register(Movimientoproducto,MovimientoproductoAdmin)
admin.site.register(Perfil,PerfilAdmin)
admin.site.register(Persona,PersonaAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Talla,TallaAdmin)
admin.site.register(Tipoestampado,TipoestampadoAdmin)
admin.site.register(Tipomovimiento,TipomovimientoAdmin)
admin.site.register(Tipotela,TipotelaAdmin)

# from import_export import resources

# class ColorResource(resources.ModelResource):

#     class Meta:
#         model = Color

# from django.contrib import admin
# from models import Enlace, Categoria, Agregador

# from actions import export_as_csv

# class EnlaceAdmin(admin.ModelAdmin):
#     list_display = ('enlace', 'titulo', 'categoria', 'imagen_voto', 'es_popular')
#     list_filter = ('categoria', 'usuario',)
#     search_fields = ('categoria__titulo', 'usuario__email')
#     list_editable = ('titulo', 'enlace', 'categoria')
#     list_display_links = ('es_popular',)
#     actions = [export_as_csv]
#     raw_id_fields = ('categoria', 'usuario')

#     def imagen_voto(self, obj):
#         url = obj.mis_votos_en_imagen_rosada()
#         tag = '<img src="%s">' % url
#         return tag
#     imagen_voto.allow_tags = True
#     imagen_voto.admin_order_field = 'votos'

# class EnlaceInline(admin.StackedInline):
#     model = Enlace
#     extra = 3
#     raw_id_fields = ('usuario',)

# class CategoriaAdmin(admin.ModelAdmin):
#     actions = [export_as_csv]
#     inlines = [EnlaceInline]




