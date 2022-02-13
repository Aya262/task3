from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bus(models.Model):
    serial_number=models.IntegerField(blank=False,null=False)
    model=models.CharField(max_length=50)
    color=models.CharField(max_length=50)

    def __str__(self):
        return str(self.serial_number)


class Station(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False)
    time_to_wait=models.IntegerField()

    def __str__(self):
        return self.name

class BusRoute(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False)
    station_start=models.ForeignKey(Station,on_delete=models.CASCADE,related_name='station_start')
    station_end=models.ForeignKey(Station,on_delete=models.CASCADE,related_name='station_end')
    station_list=models.ManyToManyField(Station)

    def __str__(self):
        return self.name

class RegistrationPeriodType(models.Model):
    name=models.CharField(max_length=50,blank=False,null=False)
    number_of_trips=models.IntegerField()
    price=models.FloatField()
    discount=models.FloatField()

    def __str__(self):
        return self.name

class Registration(models.Model):
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    bus_route=models.ForeignKey(BusRoute,on_delete=models.CASCADE)
    #start_date=models.DateField()
    #end_date=models.DateField()
    registration_type=models.ForeignKey(RegistrationPeriodType,on_delete=models.CASCADE)
    isactive=models.BooleanField(default=False)


    #payment_reciept