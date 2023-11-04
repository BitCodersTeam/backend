from django.db import models

from discord.database.member.Member import Member


class MemberActivity(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    money = models.IntegerField(default=0)

    lvl = models.IntegerField(default=0)
    exp = models.IntegerField(default=0)
    up_xp = models.IntegerField(default=50)

    class Meta:
        app_label = 'discord'

