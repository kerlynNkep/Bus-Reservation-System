#from django.contrib.auth import views as auth_views
#from rest_framework_jwt.views import refresh_jwt_token
from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from . import views


router = routers.DefaultRouter()

router.register('travelinfo', views.Listing_TravelInfo)
router.register('travelinfoAdmin', views.adminTravelInfo)
router.register('reservation', views.Reservation_list)
router.register('reservation_details', views.Reservation_Details)
router.register('bus_admin', views.Bus_listing)
router.register('bus_display', views.Bus_Details )
router.register('payment_details', views.Payment_details)


app_name = 'core'
urlpatterns = [
   path('', include(router.urls))
]
