from django.shortcuts import render
import datetime
from django import forms


#importamos esto, para que podamos usar el HttpResponse.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

#En esta función vamos a ver cómo insertar y crear varibles en HTML desde Python. 

class NewTaskForm(forms.Form):
    task = forms.CharField(label="Nueva tarea")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)

tareas = []

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
    texto = f"¡Hola, {nombre.capitalize()}!"
    return render(request, "hello/lista.html", {
        "nombre": texto
    })

def añadir(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            tareas.append(task)
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("primer_proyecto:lista"))
        
        else:
            return render(request, "hello/añadir.html", {
                "form":form
            })
    
    return render(request, "hello/añadir.html", {
        "form" : NewTaskForm() 
    })

def lista(request):
    if "tasks" not in request.session:
       
        request.session["tasks"] = []

    return render(request, "hello/lista.html", {
        "tasks" : request.session["tasks"],
        "tareas": tareas,
        }
    )
    
 