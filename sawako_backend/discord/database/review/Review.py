from django.db import models

from discord.database.guild.Guild import Guild
from discord.database.user.User import User


class Review(models.Model):
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    mark = models.IntegerField()
    comment = models.CharField(max_length=100)

    class Meta:
        app_label = 'discord'