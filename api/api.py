from tastypie.resources import ModelResource
from games.models import Game, Store
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS

class StoreResource(ModelResource):

	class Meta:
		queryset = Store.objects.all()


class GameResource(ModelResource):
	store = fields.ForeignKey(StoreResource, 'store', full=True)

	class Meta:
		queryset = Game.objects.all()
		limit = 0
		resource_name = 'games'
		filtering = {
			"name": ['startswith', 'endswith', 'contains', 'icontains'],
			"store": ALL_WITH_RELATIONS
		}