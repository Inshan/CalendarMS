from django.urls import path
from .views import *

urlpatterns = [
    path('events/', events_view, name='events_by_date'),
    path('events/<str:date>/', events_list, name='events_by_date'),
    path('holidays/', holidays_list, name = 'holidays'),
    path('error_throw/', error_throw, name = 'error_throw'),
    path('event_create/', event_create, name = 'event_create'),
    path('', calendar_view, name = 'calendar'),
]
