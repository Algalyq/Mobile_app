from django.contrib import admin
from .models import Uniforms,SeasonTicket


admin.site.register(Uniforms)

class SeasonAdmin(admin.ModelAdmin):
    list_display = ('name_season', 'price_season')
    ordering = ('name_season', 'price_season')
    

admin.site.register(SeasonTicket,SeasonAdmin)
    