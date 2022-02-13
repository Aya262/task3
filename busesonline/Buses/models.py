from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group,Permission
from django.contrib.contenttypes.models import ContentType
# Create your models here.

#admins_group,created=Group.objects.get_or_create(name='Admins')
#ct=ContentType.objects.get_for_model(User)
#permission=Permission.objects.create(codename='activate_reservation',
#                                                name='activate_reservation',
#                                                content_type=ct)
#admins_group.permissions.add(permission)                                          

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
    recide_number=models.IntegerField()
    isactive=models.BooleanField(default=False)

    def __str__(self):
        return self.customer.username
    #payment_reciept