from django.shortcuts import render

from .models import Flight
# Create your views here.

def flights(request):
    return render(request, "flights/index.html",{
        #Recuerda que Flight es la clase, puedes remplazar Flight por otra clase de models.
        "flights" : Flight.objects.all()
    })



def passengers(request):
    return render(request, "flights/index.html")

def origins(request):
    return render(request, "flights/index.html")