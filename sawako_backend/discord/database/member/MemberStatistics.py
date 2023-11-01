from django.db import models

from discord.database.member.Member import Member


class MemberStatistics(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    messages = models.IntegerField()
    voice = models.IntegerField()

    class Meta:
        app_label = 'discord'