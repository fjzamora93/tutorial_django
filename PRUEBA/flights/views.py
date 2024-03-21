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
    return render(request, "flights/flight_detail.html", {"flight": flight})

