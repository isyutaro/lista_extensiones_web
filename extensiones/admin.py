from extensiones.models import Departamento, Todo
from django.contrib import admin

class buscaTodo(admin.ModelAdmin):
	list_display = ('nombre', 'mail', 'telefono', 'extension', 'depto', 'activo')
	list_per_page = 25
	ordering = ('nombre',)
	search_fields = ['nombre', 'mail', 'extension', 'depto__nombre',]
	list_filter =['depto__nombre', 'activo',]

admin.site.register(Todo, buscaTodo)

class buscaDepto(admin.ModelAdmin):
	list_display = ('nombre',)
	list_per_page = 25
	ordering = ('nombre',)
	search_fields = ['nombre',]

admin.site.register(Departamento, buscaDepto)
