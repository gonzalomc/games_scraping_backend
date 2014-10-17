from django.contrib import admin
from games.models import Store, Game, Console, GameAdmin

# Register your models here.

admin.site.register(Store)
admin.site.register(Game, GameAdmin)
admin.site.register(Console)