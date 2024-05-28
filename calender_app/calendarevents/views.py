from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from django.shortcuts import render, redirect
import pytz


TIMEZONE_CHOICES = [(tz, tz) for tz in pytz.all_timezones]


def events_list(request):
    evented = Event.objects.all()
    return render(request, "events.html", {"evented": evented})

def event_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        start_time = request.POST.get("start_time")
        end_time = request.POST.get("end_time")
        timezone = request.POST.get("timezone")
        
        if timezone not in dict(TIMEZONE_CHOICES):
            timezone = 'UTC'  # Default to 'UTC' if the provided timezone is not valid

        obj = Event.objects.create(
            title=title,
            description=description,
            start_time=start_time,
            end_time=end_time,
            timezone=timezone
        )
        return redirect("calendar")  # Ensure you have a URL pattern named 'calendar'
    return render(request, "event_create.html", {"timezone_choices": TIMEZONE_CHOICES})


def holidays_list(request):
    # Fetch holidays from an API or a static list
    holidays = [
        {"name": "New Year's Day", "date": "2024-01-01"},
        {"name": "Christmas Day", "date": "2024-12-25"},
        # Add more holidays as needed
    ]
    return render(request, "holidays.html", {"holidays": holidays})


def calendar_view(request):
    return render(request, "calendar.html")
