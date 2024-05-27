from django.urls import path
from .views import *

urlpatterns = [
    path('events/', events_list, name='events'),
    path('holidays/', holidays_list, name = 'holidays'),
    path('event_create/', event_create, name = 'event_create'),
    path('', calendar_view, name = 'calendar'),
]
