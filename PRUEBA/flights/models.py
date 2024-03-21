from django.db import models


class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"
    

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals", default=None)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: desde {self.origin} hasta {self.destination}"
    

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)

    #ASÍ ES COMO SE CONSTRUYE UNA TABLA QUE VA A IR DE MUCHOS A MUCHOS
        #blank permite que no tenga flights...
        #¿qué es lo que hace el related_name? AVERIGUAR
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first}, {self.last}"