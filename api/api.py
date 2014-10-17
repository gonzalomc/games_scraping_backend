from tastypie.resources import ModelResource
from games.models import Game, Store, Console
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS

class StoreResource(ModelResource):

	class Meta:
		queryset = Store.objects.all()


class ConsoleResource(ModelResource):

	class Meta:
		queryset = Console.objects.all()
		

class GameResource(ModelResource):
	store = fields.ForeignKey(StoreResource, 'store', full=True)
	console = fields.ForeignKey(ConsoleResource, 'console', full=True)

	class Meta:
		queryset = Game.objects.all()
		limit = 0
		resource_name = 'games'
		filtering = {
			"name": ['startswith', 'endswith', 'contains', 'icontains'],
			"store": ALL_WITH_RELATIONS,
			"console": ALL_WITH_RELATIONS
		}