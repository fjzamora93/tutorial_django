Para trabaja con Django lo primero que tenemos que hacer es instalarlo 
en nuestro PC. Así que en primer lugar haremos lo siguiente:

        pip3 install Django

Seguidamente, será necesario crear un nuevo proyecto de django,
para lo que ejecutaremos el siguiente comando:

        django-admin startproject PROJECT_NAME

¿Qué hacen las distintas carpetas?
-manage: no hay que tocarla. Es el archivo que se usa para ejecutar comandos.
-Settings: configuración importante. Viene precargada, pero podemos añadir características.
-urls: es una tabla de contenido de nuestra web aplication que podemos visitar.

CORRER E INTERRUMPIR EL SERVIDOR

El siguiente paso es introducir el comando para poner a funcionar el servidor:

        python manage.py runserver

Podemos interrumpir la ejecución del servidor con el siguiente comando:

        ctrl + c

Al ejecutar este comando, asegúrate de estar en la misma carpeta que el archivo manage.py

Nos va a devolver unos errores, y además, nos va a devolver esto:
Starting development server at http://127.0.0.1:8000/
En otras palabras, una dirección a la que SOLO nosotros podemos acceder.


CREACIÓN DE UNA APLICACIÓN

Un proyecto de DJANGO tiene varias aplicaciones.
La cuestión es integrar todas estas aplicaciones dentro de un mismo marco.
Para eso, podemo empezar creando una primera aplicación.

    python manage.py startapp hello

--al correr este comando, se nos creará un nuevo directorio con la nueva aplicación.
--en este caso, se nos habrá creado la carpeta hello, justo en este punto.

VAMOS A Settings

Si bajamos en settings, encontraremos una sección llamada "INSTALLED_APPS" = []
Lo que tenemos que hacer aquí es añadir la nueva aplicación creada que queramos agregar.
Tal que así:

INSTALLED_APPS = [
    'hello',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

Ahora lo qu ehay que hacer es que esta app haga algo. Para conseguirlo, vamos aldirectorio Hello
y buscamos view. Una view es algo que queremos ver. Así que vamos a crear una por defecto.
Esto lo podemos ver en views.

UNA URL PARTICULAR
Aunque django tiene el archivo de URL para mantener todas las apps aglutinadas,
quizás nos interesa crear un archivo url para cada aplicación web por separado.
Así que nos vamos a nuestra app, y creamos un archivo urls.py.
El archivo lo podemos rellenar tal y como vemos en URLS.PY de la carpeta hello.

AÑADIR A LAS URLS GENERALES
Ahora, debemos integrar esto en las URLS del proyecto global.
Para ello, nos aseguramos de importar las funciones necesarias (path, include, etc..)
y además agregamos la nueva URL con todos los rutas de dicha url. 
Se vería algo así:

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include("hello.urls"))
]