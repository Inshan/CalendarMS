# Generated by Django 4.2.10 on 2024-05-28 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendarevents', '0002_alter_event_timezone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='timezone',
        ),
    ]
