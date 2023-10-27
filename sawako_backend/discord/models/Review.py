from django.db import models

from discord.models.Guild import Guild
from discord.models.User import User


class Review(models.Model):
    guild = models.ForeignKey(Guild, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.SET_NULL)

    mark = models.IntegerField(max_length=5)
    comment = models.CharField(max_length=100)