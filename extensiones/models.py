from django.db import models
from datetime import datetime

class Departamento(models.Model):
	nombre = models.CharField("Nombre", max_length="100")

	def __unicode__(self):
		return u'%s' % (self.nombre)

	class Meta:
		ordering = ['nombre']

class Todo(models.Model):
	nombre = models.CharField("Nombre Completo", max_length="200")
	mail = models.EmailField("e-mail", null=True, primary_key=True)
	telefono = models.CharField("Telefono", max_length = "14", blank=True, null=True)
	depto = models.ForeignKey(Departamento, verbose_name="Departamento")
	extension = models.IntegerField("Extension", max_length="3")
	activo = models.BooleanField("Usuario activo?", default=True)

	def __unicode__(self):
		return u'%s' % (self.nombre)

	class Meta:
		ordering = ['nombre']
