from django.db import models
import pytz

TIMEZONE_CHOICES = [(tz, tz) for tz in pytz.all_timezones]

class Event(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    timezone = models.CharField(max_length=63, choices=TIMEZONE_CHOICES, default='UTC')
    
    def __str__(self):
        return self.title
