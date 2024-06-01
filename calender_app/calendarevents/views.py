from rest_framework.decorators import api_view
from .models import Event
from django.shortcuts import render, redirect
import pytz
import requests
from dateutil.parser import parse
from datetime import datetime
from django.urls import reverse

TIMEZONE_CHOICES = [(tz, tz) for tz in pytz.all_timezones]


def events_list(request, date):
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    events = Event.objects.filter(start_time__date=date_obj)

    if not events:
        return render(request, "events.html", {"message": "No events registered"})

    return render(request, "events.html", {"events": events, "date_obj": date_obj})


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
    # Calendarific API endpoint
    api_url = "https://calendarific.com/api/v2/holidays"

    # Calendarific API key (replace "YOUR_API_KEY" with your actual API key)
    api_key = "nI8eR3fGqMzh5i2m1loHoT96BPjF5zfa"

    # Country code and year for which you want to fetch holidays
    country_code = "NP"  # Example: Nepal
    year = 2024  # Example: 2024

    # Make the API request
    response = requests.get(api_url, params={"api_key": api_key, "country": country_code, "year": year})

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract holiday information from the response
        holidays = data.get("response", {}).get("holidays", [])

        # Prepare data for calendar rendering
        holidays_data = []
        for holiday in holidays:
            holiday_date = parse(holiday['date']['iso']).replace(tzinfo=None)
            holidays_data.append({
                'name': holiday['name'],
                'date': holiday_date,
                'day': holiday_date.day,
                'month': holiday_date.month,
                'year': holiday_date.year,
            })

        # Sort holidays by year, month, and day
        # holidays_data.sort(key=lambda x: (x['day'], x['month'], x['year']))

        # Render the template with the extracted holiday data
        return render(request, "holidays.html", {"holidays_data": holidays_data})
    else:
        # If the request was not successful, handle the error
        message = "Failed to fetch holidays. Status code: {}".format(response.status_code)
        return render(request, 'error_throw.html',{"message":message})


def calendar_view(request):
    return render(request, "calendar.html")


def error_throw(request):
    message = request.GET.get('message', 'An error occurred.')
    return render(request, "error_throw.html", {"message":message})