from django.db import models

# Create your models here.
class Store(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class Game(models.Model):
	name = models.CharField(max_length=200, null=True, blank=True)
	price = models.CharField(max_length=20, null=True, blank=True)
	store = models.ForeignKey(Store)

	def __unicode__(self):
		return "%s - %s" % (self.name, self.price)
