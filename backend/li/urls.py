
from django.conf.urls import url, include
from rest_framework import routers                    # add this
from li.views import *                            # add this

router = routers.DefaultRouter()                      # add this
router.register(r'phonenumber', PhoneNumbersView) 

urlpatterns = [
    url(r'api/', include(router.urls)),    
    url(r'phonenumber/', include(router.urls))             
]