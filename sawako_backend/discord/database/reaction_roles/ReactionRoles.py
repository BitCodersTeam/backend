from django.db import models

from discord.database.guild.Guild import Guild


class ReactionRoles(models.Model):
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE)
    message = models.BigIntegerField()
    reaction = models.CharField(max_length=30)
    type = models.SmallIntegerField()
    object = models.BigIntegerField()

    class Meta:
        app_label = 'discord'