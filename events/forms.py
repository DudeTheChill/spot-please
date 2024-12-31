from django.forms import ModelForm
from .models import Event


class EventCreateForm(ModelForm):

    class Meta:
        model = Event
        fields = ['title', 'date_and_time', 'location', 'show_type']

class EventbriteForm(ModelForm):

    class Meta:
        model = Event
        fields = ['eventbrite_url']