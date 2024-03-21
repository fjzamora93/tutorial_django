from django.urls import path
from django.contrib import admin
from . import views


from .models import Flight

urlpatterns=[
    #Introducimos el admin
    path('admin/', admin.site.urls),

    #Utilizaremos una view para mostrar los detalles de cada vuelo en particucar
    path("<int:flight_id>", views.flights_detail, name="flight_detail"),

    path("", views.index, name="index"), 
    
]
