from django.db import models

from discord.models.Guild import Guild


class ReactionRoles(models.Model):
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE)
    message = models.BigIntegerField()
    reaction = models.CharField(30)
    type = models.SmallIntegerField()
    object = models.BigIntegerField()