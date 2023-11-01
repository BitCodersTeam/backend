
from django import forms

from discord.database.guild.Guild import Guild


class GuildForm(forms.ModelForm):
    class Meta:
        model = Guild
        fields = ('id',)