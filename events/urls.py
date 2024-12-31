from django.urls import path
from .views import 

urlpatterns = [
    path('', , name="events-home"),
    path('create_choices/', , name="event-create"),
    path('create/', , name="event-form"),
    path('create_with_eventbrite/', , name="event-brite"),
    path('update/<int:pk>/', , name="event-update"),
    path('delete/<int:pk>/', , name="event-delete"),
    path('delete_confirmation/<int:pk>/', , name="event-delete-confirm"),
    path('<int:pk>/', , name="event-details"),
]