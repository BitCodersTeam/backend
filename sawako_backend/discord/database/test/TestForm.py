from django import forms

from discord.database.test.Test import Test


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ('name', 'image')