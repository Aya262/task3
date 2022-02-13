from django.urls import path
from .views import *
urlpatterns=[

    path('',index,name='index'),
    path('accounts/sign_up',sign_up,name='sign_up'),
    #path('reserve/<int:rout_id>/<int:reg_id>/',reserve,name='reserve'),
    path('home/',home,name='home'),
    path('inactiveReservations/',inactivate_reservations,name='inactive_reservation'),
    path('activate/<int:reserve_id>/',active_reservation,name='activate')
]