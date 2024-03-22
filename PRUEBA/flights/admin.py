from django.contrib import admin

# Register your models here.
from .models import Flight, Airport, Passenger


"""
Ahora vamos a configurar este panel de una forma muy concreta.
La clase de abajo es un display
"""

class FlightAdmin(admin.ModelAdmin):
    list_display = ("origin", "destination", "duration", "id")

class PassengerAdmin(admin.ModelAdmin):
    fliter_horizontal = ("flights", )


admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
