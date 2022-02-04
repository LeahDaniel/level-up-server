from django.db import models

from .event_gamer import EventGamer
from .game import Game
from .gamer import Gamer


class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="events")
    organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE, related_name="organizing")
    attendees = models.ManyToManyField(Gamer, through=EventGamer, related_name="attending")
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    
    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value
