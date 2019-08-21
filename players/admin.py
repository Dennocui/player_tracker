from django.contrib import admin

from .models import Player, Club, Position, Role, High_school 

admin.site.register(Player)
admin.site.register(Role)
admin.site.register(Position)
admin.site.register(High_school)
admin.site.register(Club)

