from django import forms
from . import models


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'body', 'image']


class ReviewForm(forms.ModelForm):
    CHOICES = [0, 1, 2, 3, 4, 5]
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    class Meta:
        model = models.Review
        fields = ['headline', 'body']

