from django.urls import path
from .views import *
urlpatterns=[

    path('',index,name='index'),
    path('accounts/sign_up',sign_up,name='sign_up'),
    path('home/',home,name='home'),
    path('reserve/<int:rout_id>/<int:reg_id>/',reserve,name='reserve'),
    path('home2/',home2,name='home2')
]