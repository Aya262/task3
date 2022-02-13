from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Bus)
admin.site.register(Station)
admin.site.register(BusRoute)
admin.site.register(Registration)
admin.site.register(RegistrationPeriodType)
