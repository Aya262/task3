from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import Reservation
from  django.contrib import messages
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
    form=Reservation()
    if request.method=='POST':
        user=User.objects.get(username=request.user.username)
        form=Reservation(request.POST,instance=user)
        if form.is_valid():
            data=form.cleaned_data
            obj=Registration(customer=user,bus_route=data['bus_route'],registration_type=data['registration_type'],recide_number=data['recide_number'])
            obj.save()
            print("yes")
            messages.info(request,"The Reservation is Done wait for admin to activate")
    context={'form':form}
    return render(request,'Buses/home.html',context)


#@group_required('admin')
def inactivate_reservations(request):
    all_reservation=Registration.objects.filter(isactive=False)
    context={'all_reservation':all_reservation}
    return render(request,'Buses/inactive_reservations.html',context)

#@group_required('admin')
def active_reservation(request,reserve_id):
    reservation=Registration.objects.get(id=reserve_id)
    reservation.isactive=True
    reservation.save()
    return render(request,'Buses/activation_done.html')

    