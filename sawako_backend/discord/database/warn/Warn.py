from django.db import models

from discord.database.member.Member import Member


class Warn(models.Model):
    moderator = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
    target = models.ForeignKey(Member, on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=30)

    class Meta:
        app_label = 'discord'
