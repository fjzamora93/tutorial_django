from django.shortcuts import render

from .models import Flight
# Create your views here.

def index(request):
    return render(request, "flights/index.html",{
        #Recuerda que Flight es la clase, puedes remplazar Flight por otra clase de models.
        "flights" : Flight.objects.all()
    })



def flights_detail(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight_detail.html", {
        "flight": flight,

        #Fíjate que al dar acceso estamos usando "passengers", que es el 'RELATED NAME' que le dimos.
        #Al mismo tiempo, para dar acceso a la lista de todos, añadimso el all
        "passengers" : flight.passengers.all(),
        })

