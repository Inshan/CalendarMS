from django.db import models
import pytz

class Event(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    timezone = models.CharField(max_length=50)

    def __str__(self):
        return self.title
