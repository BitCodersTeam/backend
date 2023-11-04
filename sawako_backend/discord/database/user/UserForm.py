from django import forms

from discord.database.user.User import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id', 'settings']