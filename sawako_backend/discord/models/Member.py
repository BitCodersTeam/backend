from django.db import models

from discord.models.Guild import Guild
from discord.models.User import User


class Member(models.Model):
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    birthdate = models.CharField(max_length=5)
    about = models.CharField(max_length=10)

    class Meta:
        unique_together = ('guild', 'user')