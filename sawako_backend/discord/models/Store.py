from django.db import models

from discord.models.Guild import Guild


class Store(models.Model):
    guild = models.ForeignKey(Guild, on_delete=models.CASCADE)

    item = models.BigIntegerField()
    type = models.SmallIntegerField()
    name = models.CharField(max_length=10)
    description = models.CharField(max_length=20)
    price = models.IntegerField()