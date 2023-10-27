from django.db import models

from discord.models.Member import Member


class Pair(models.Model):
    pair1 = models.ForeignKey(Member, unique=True, on_delete=models.CASCADE)
    pair2 = models.ForeignKey(Member, unique=True, on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now_add=True)