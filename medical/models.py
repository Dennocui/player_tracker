from django.db import models
from django.utils import timezone

from players import models as Player

class Medical(models.Model):
    player = models.ForeignKey(Player.Player, on_delete=models.CASCADE)
    injury_type = models.CharField(max_length=225)
    injury_date = models.DateField()
    injury_comments = models.CharField(max_length=255, null=True) 
    recovery_date = models.DateField()
    conditioning_notes = models.CharField(max_length=225, null=True)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "{}  {}".format(self.player.first_name[:25], self.player.last_name[:25])

    def days_left(self):
    	return self.recovery_date.day - timezone.now().day
