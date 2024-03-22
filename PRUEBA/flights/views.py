from django.shortcuts import render

from django.db.models import Subquery, OuterRef

from .models import Flight, Passenger
# Create your views here.

from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(request, "flights/index.html",{
        #Recuerda que Flight es la clase, puedes remplazar Flight por otra clase de models.
        "flights" : Flight.objects.all()
    })



def flights_detail(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)

    #Para el booking, vamos a crear un campo que sea los que no están en un vuelo en particular
    #Para ello vamos a usar EXCLUDE, ¿y qué exclude? lo que tiene coincidencia entre flights y flight.
    #Y para rematar, le decimos que nos los busque a todos .ALL()

    non_passengers = Passenger.objects.exclude(flights = flight).all()

    return render(request, "flights/flight_detail.html", {
        "flight": flight,

        #Fíjate que al dar acceso estamos usando "passengers", que es el 'RELATED NAME' que le dimos.
        #Al mismo tiempo, para dar acceso a la lista de todos, añadimso el all
        "passengers" : flight.passengers.all(),

        "non_passengers" : non_passengers
        })



#Con la siguiente vista damos la posibilidad de que un usuario se registre en un vuelo.

def book(request, flight_id):
    if request.method == "POST":
        #PASO 1. Obtenemos la id de un vuelo en cuestión
        flight = Flight.objects.get(pk = flight_id)

        #PASO2. A partir del formulario, obtenemos la id del pasajero
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))

        #PASO3. Añadimos el vuelo (a partir de su ID) a la lista de vuelos del pasajero
        passenger.flights.add(flight)

        #PASO 4. Volvemos atrás y vamos los detalles del vuelo con la id del vuelo facilitado
        return HttpResponseRedirect(reverse("flight_detail", args=[flight_id]))