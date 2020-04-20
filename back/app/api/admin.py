from django.contrib import admin

# Register your models here.

from .models import (
    Country,
    City,
    Stadium,
    Team,
    Person,
    Player,
    Coach
)


admin.site.register(Country)
admin.site.register(City)
admin.site.register(Stadium)
admin.site.register(Team)
admin.site.register(Person)
admin.site.register(Player)
admin.site.register(Coach)