from django import forms

from discord.database.member.Member import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['guilds', 'user']