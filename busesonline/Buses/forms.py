from .models import *
from django.forms import ModelForm
class Reservation(ModelForm):
    class Meta:
        model=Registration
        fields=['bus_route','registration_type','recide_number']    
