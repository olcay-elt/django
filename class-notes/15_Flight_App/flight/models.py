from django.db import models
from django.contrib.auth.models import User


class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    operation_airlines = models.CharField(max_length=15)
    departure_city = models.CharField(max_length=30)
    arrival_city = models.CharField(max_length=30)
    date_of_departure = models.DateField()
    etd = models.TimeField()

    def __str__(self):
        return f'{self.flight_number} - {self.departure_city} - {self.arrival_city}'
    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="reservations")
    passenger = models.ManyToManyField(Passenger, related_name="reservation")
    
    
