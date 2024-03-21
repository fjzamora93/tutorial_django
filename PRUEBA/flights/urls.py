from django.urls import path
from django.contrib import admin
from . import views


from .models import Flight

urlpatterns=[
    #Introducimos el admin
    path('admin/', admin.site.urls),

    path("", views.flights, name="index"), #Cuando alguien visite la url vacía, verá la index.
    path("flights", views.flights, name="flights"),
    path("passengers", views.passengers, name="passenger"),
    path("origins", views.origins, name="origins" ),
]
