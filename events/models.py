from django.db import models
from django.contrib.auth.models import User

SHOW_TYPE_CHOICES = [
    ("COM", "Curated Open Mic"),
    ("SHW", "Showcase"),
    ("S2G", "Show Up to Go Up"),
]

class Event(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField()
    location = models.CharField(max_length=50)
    show_type = models.CharField(max_length=3, choices=get_currencies)
    eventbrite_url = models.URLField(max_length=600)

    def __str__(self):

        return f"Even Created by {self.owner}"

    def create_with_eventbrite(self):

        pass