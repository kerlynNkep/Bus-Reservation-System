from rest_framework import serializers
from django.contrib.auth.decorators import login_required
from .models import TravelList, Bus, UserProfile, Payment, Reservation
from django.contrib.auth import authenticate, user_logged_in


class TravelListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TravelList
        fields = ('Pickup_Point', 'Day', 'Destination')

class BusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bus
        fields = ('BusNumber', 'BusName', 'NumberOfSeats')

class UserProfileSerializer (serializers.ModelSerializer):
    class Meta:
        model = UserProfile 
        fields = ('website', 'picture', 'user')

class PaymentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('payment_status', 'payment_type', 'account_Number', 'account_Name', 'reservation')


class ReservationSerializer (serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('user', 'travelInfo')