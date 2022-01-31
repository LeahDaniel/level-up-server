from django.db import models

from .gamer import Gamer
from .gameType import GameType


class Game(models.Model):
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    number_of_players = models.PositiveIntegerField()
    skill_level = models.PositiveIntegerField()
