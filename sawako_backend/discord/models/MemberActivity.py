from django.db import models

from discord.models.Member import Member


class MemberActivity(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    money = models.IntegerField(default=0)

    lvl = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    up_xp = models.IntegerField(default=50)

