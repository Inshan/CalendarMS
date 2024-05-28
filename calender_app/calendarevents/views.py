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


import requests
from django.shortcuts import render

def holidays_list(request):
    # Calendarific API endpoint
    api_url = "https://calendarific.com/api/v2/holidays"

    # Calendarific API key (replace "YOUR_API_KEY" with your actual API key)
    api_key = "nI8eR3fGqMzh5i2m1loHoT96BPjF5zfa"

    # Country code and year for which you want to fetch holidays
    country_code = "NP"  # Example: United States
    year = 2024  # Example: 2024

    # Make the API request
    response = requests.get(api_url, params={"api_key": api_key, "country": country_code, "year": year})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract holiday information from the response
        holidays = data.get("response", {}).get("holidays", [])

        # Render the template with the extracted holiday data
        return render(request, "holidays.html", {"holidays": holidays})
    else:
        # If the request was not successful, handle the error
        error_message = "Failed to fetch holidays. Status code: {}".format(response.status_code)
        return render(request, "error.html", {"error_message": error_message})


def calendar_view(request):
    return render(request, "calendar.html")
