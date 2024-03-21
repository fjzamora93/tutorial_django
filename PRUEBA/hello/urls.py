from django.urls import path
from . import views


"""
La siguiente línea de código app_name = "name", lo que hará será prevenir
colisión entre páginas que tengan el mismo name = "". 

De esta forma, a partir de ahora las rutas relativas deberán especificar también el nombre
de la app que se esté utilizando para que puedan utilizar el href de la app adecuada.

Esto sucederá especialmente cuando varias páginas se llamen index... o style
"""
app_name = "primer_proyecto"


urlpatterns=[
    
    path("", views.index, name="index"), #Cuando alguien visite la url vacía, verá la index.
    path("añadir", views.añadir, name="añadir"),
    path("potion-craft", views.potion_craft, name="potion"),
    path("lista", views.lista, name="lista" ),
    path("javi", views.javi, name="javi"),
    path("<str:nombre>", views.saludo, name="saludo"),
    
    
    
]

"""
Si nos fijamos, el método path recibe tres parámetros:
1. El primero es la URL. Si no hay nada, será el index... Si hay algo, será lo que metamos.
2. El segundo parámetro es la FUNCIÓN  a la que está llamando desde VIEWS.
3. El tercer parámetro, name, es simplemente para que sea más fácil referenciar cada URL.

"""