
from django.db import models

from cricket_info.models.players_info import PlayersInfo


class PlayersHistory(models.Model):
    player = models.ForeignKey(PlayersInfo, models.DO_NOTHING, blank=True, null=True)
    matches = models.IntegerField(blank=True, null=True)
    run = models.IntegerField(blank=True, null=True)
    highest_scores = models.IntegerField(blank=True, null=True)
    fifties = models.IntegerField(blank=True, null=True)
    hundred = models.IntegerField(blank=True, null=True)
    createdAt = models.DateTimeField(db_column='createdAt')  

    class Meta:
        managed = False
        db_table = 'players_history'
