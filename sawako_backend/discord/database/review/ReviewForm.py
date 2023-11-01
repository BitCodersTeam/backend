from django import forms

from discord.database.review.Review import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['guilds', 'user', 'mark', 'comment']