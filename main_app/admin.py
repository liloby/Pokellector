from django.contrib import admin
from .models import Pokemon, Interaction, Move
# Register your models here.
admin.site.register(Pokemon)
admin.site.register(Interaction)
admin.site.register(Move)
