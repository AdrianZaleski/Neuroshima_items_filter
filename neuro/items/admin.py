from django.contrib import admin

from .models import Difficulty, Damage, Weapon, Ammo, Ranged

admin.site.register(Difficulty)
admin.site.register(Damage)
admin.site.register(Weapon)
admin.site.register(Ammo)
admin.site.register(Ranged)
