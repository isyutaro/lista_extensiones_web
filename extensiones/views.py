from django.shortcuts import render_to_response
from extensiones.models import *
from django.db.models import Q
from django.core.cache import cache

def extensiones(request):
	if 'qbusca' in request.GET:
		q = request.GET['qbusca']
		mc = cache.get(q)
		if not mc:
			ext = Todo.objects.filter(
				Q(extension__icontains=q) | 
				Q(nombre__icontains=q) | 
				Q(depto__nombre__icontains=q),
				Q(activo=True)
			)
			ext = ext.order_by("nombre")
			cache.set(q, ext, 60*60*6)
			print ">>> set item"
		else:
			ext = mc
			print ">>> cached item"
	else:
		mc = cache.get('todo')
		if not mc:
			ext = Todo.objects.filter(activo=True)
			ext = ext.order_by("nombre")
			cache.set('todo', ext, 60*60*6)
			print ">>> set item"
		else:
			ext = mc
			print ">>> cached item"

	d = []
	for i in ext:
		d.append(i.depto)
	dep = dict.fromkeys(d).keys()
	dep = sorted(dep, key=lambda Departamento:Departamento.nombre)
	return render_to_response('extensiones.html', {'dep': dep, 'ext': ext})
