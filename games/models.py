from django.db import models
from django.contrib import admin
# Create your models here.
class Store(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name


class Console(models.Model):
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name


class Game(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	price = models.CharField(max_length=20, null=True, blank=True)
	store = models.ForeignKey(Store)
	console = models.ForeignKey(Console)

	def __unicode__(self):
		return "%s - %s" % (self.name, self.price)

class GameAdmin(admin.ModelAdmin):
	list_filter = ('store', 'console', )
