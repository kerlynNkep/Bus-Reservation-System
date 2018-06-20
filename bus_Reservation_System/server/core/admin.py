from django.contrib import admin
from .models import TravelList, Bus, UserProfile, Payment, Reservation

admin.site.register(TravelList)
admin.site.register(Bus)
admin.site.register(UserProfile)
admin.site.register(Payment)
admin.site.register(Reservation)
