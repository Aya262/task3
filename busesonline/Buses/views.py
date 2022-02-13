from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import Reservation
# Create your views here.

def index(request):
    return render(request,'Buses/index.html')

def sign_up(request):
    form=UserCreationForm()
    if request.method=='post':
        if form.is_valid():
            user=form.save()
            login(request,user)
            return render(request,'Buses/index.html')
    context={'form':form}
    return render(request,'registration/sign_up.html',context)
    

@login_required
def home(request):
    #customer=User.objects.get(id=cust_id)
    bus_routes=BusRoute.objects.all()
    register_type=RegistrationPeriodType.objects.all()
    context={
        #'customer':customer,
        'bus_routes':bus_routes,
        'register_type':register_type
    }
    return render(request,'Buses/home.html',context)

def home2(request):
    form=Reservation()
    if request.method=='POST':
        user=User.objects.get(username=request.user.username)
        print(user)
        print("====================================================================================")
        print(request.POST)
        print("====================================================================================")
        form=Reservation(request.POST,instance=user)
        if form.is_valid():
            form.save()
            print("Registration Done")
            print("====================================================================================")

    context={'form':form}
    return render(request,'Buses/home2.html',context)



def reserve(request,rout_id,reg_id):
    registrationtype_obj=RegistrationPeriodType.objects.get(id=reg_id)
    bus_route_obj=BusRoute.objects.get(id=rout_id)
    #customer_obj=User.objects.get(id=cut_id)
    registration_obj=Registration(bus_route=bus_route_obj,registration_type=registrationtype_obj)
    form=Reservation()
    if request.method=='post':
        form=Reservation(request.POST,instance=registration_obj)
        if form.is_valid():
            form.save()
            print("yes")
    context={'form':form}
    return render(request,'Buses/reserve.html',context)
    