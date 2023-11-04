from django.db import models

from discord.database.guild.Guild import Guild
from discord.database.user.User import User


class Member(models.Model):
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=10, default='Не указано')
    gender = models.CharField(max_length=10, default='Не указано')
    birthdate = models.CharField(max_length=5, default='Не указано')
    about = models.CharField(max_length=10, default='Отсутствует')

    class Meta:
        app_label = 'discord'
        unique_together = ('guild', 'user')
