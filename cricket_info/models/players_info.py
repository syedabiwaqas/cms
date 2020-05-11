from django.db import models

from cricket_info.models.team_detail import TeamDetail


class PlayersInfo(models.Model):
    team = models.ForeignKey(TeamDetail, models.DO_NOTHING, blank=True, null=True)
    first_name = models.CharField(max_length=225, blank=True, null=True)
    last_name = models.CharField(max_length=225, blank=True, null=True)
    image_url = models.CharField(max_length=225, blank=True, null=True)
    jearsy_no = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'players_info'
