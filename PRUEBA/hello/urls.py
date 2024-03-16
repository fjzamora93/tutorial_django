from django.urls import path
from . import views


urlpatterns=[
    
    path("", views.index, name="hello"), #Cuando alguien visite la url vacía, verá la index.
    path("javi", views.javi, name="javi"),
    path("<str:nombre>", views.saludo, name="saludo"),
    
]

"""
Si nos fijamos, el método path recibe tres parámetros:
1. El primero es la URL. Si no hay nada, será el index... Si hay algo, será lo que metamos.
2. El segundo parámetro es la FUNCIÓN  a la que está llamando desde VIEWS.
3. El tercer parámetro, name, es simplemente para que sea más fácil referenciar cada URL.

"""