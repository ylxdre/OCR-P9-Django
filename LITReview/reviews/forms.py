from django import forms
from . import models


class TicketForm(forms.ModelForm):
    """
    Form from Ticket, select only 3 fields
    """
    class Meta:
        model = models.Ticket
        fields = ['title', 'desc', 'image']


class ReviewForm(forms.ModelForm):
    """
    Form from Review
    Make rating field a radio select from choices
    """
    CHOICES = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'comment']


class ToFollowForm(forms.Form):
    """
    Form asking for a username
    """
    user = forms.CharField(label="Nom d'utilisateur", max_length=50)
