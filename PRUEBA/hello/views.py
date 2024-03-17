from django.shortcuts import render
import datetime

#importamos esto, para que podamos usar el HttpResponse.
from django.http import HttpResponse

# Create your views here.

#En esta función vamos a ver cómo insertar y crear varibles en HTML desde Python. 

def index(request):
    #Paso 1, definimos la variable
    now = datetime.datetime.now()
    return render(request, "hello/index.html", {
        "newyear": now.month == 1 and now.day == 1
        }
    )

"""
En el caso anterior lo primero era importar datetime.

"""


#http://127.0.0.1:8000/hello/javi
#Si visito esta URL, ahora la request será la siguiente
def javi(request):
    return HttpResponse("Hola, Javi!")


#Ahora vamos a crear una función que recibe un parámetro... un nombre... Recordamos el RENDER
#Este nombre podrá usarse como un PARÁMETRO en HTML, que se hará con {{  }}
def saludo(request, nombre):
    tasks = ["tarea 1", "tarea 2", "tarea 3"]
    return render(request, "hello/render.html", {
        "nombre":nombre.capitalize(), 
        "tareas": tasks
    })

def añadir(request):
    return render(request, "hello/añadir.html")