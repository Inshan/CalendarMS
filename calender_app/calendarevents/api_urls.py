from rest_framework import routers
from django.urls import path, include
from .api_views import *
from .models import *


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()

router.register(r'evented',EventViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]