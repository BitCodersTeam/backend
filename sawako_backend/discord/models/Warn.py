from django.db import models

from discord.models.Member import Member


class Warn(models.Model):
    moderator = models.ForeignKey(Member, on_delete=models.SET_NULL)
    target = models.ForeignKey(Member, on_delete=models.SET_NULL)

    date = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(30)
