from django.shortcuts import render
from django.db.models import Subquery, OuterRef
from django.http import HttpResponseRedirect
from django.urls import reverse

#PROCESO DE AUTENTICACIÓN
from django.contrib.auth import authenticate, login, logout

def index(request):
    if not request.user.is_authenticated:
        return (HttpResponseRedirect(reverse("login")))
    
    return render(request, "users/user.html")
    
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username= username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "user/login.html", {
                "message" : "Ha fallado el autentificar"
            })

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message" : "Logged Out",
    })