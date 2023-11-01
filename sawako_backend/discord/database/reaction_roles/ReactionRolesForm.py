
from django import forms

from discord.database.reaction_roles.ReactionRoles import ReactionRoles


class ReactionRolesForm(forms.ModelForm):
    class Meta:
        model = ReactionRoles
        fields = ['guilds', 'message', 'reaction', 'type', 'object']