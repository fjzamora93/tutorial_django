from django.shortcuts import render

#importamos esto, para que podamos usar el HttpResponse.
from django.http import HttpResponse

# Create your views here.

#este comando es así... requiere ese parámetro porque sí.
def index(request):
    return render(request, "hello/index.html")



#http://127.0.0.1:8000/hello/javi
#Si visito esta URL, ahora la request será la siguiente
def javi(request):
    return HttpResponse("Hola, Javi!")


#Ahora vamos a crear una función que recibe un parámetro... un nombre... Recordamos el RENDER
#Este nombre podrá usarse como un PARÁMETRO en HTML, que se hará con {{  }}
def saludo(request, nombre):
    return render(request, "hello/render.html", {
        "nombre":nombre.capitalize()
    })