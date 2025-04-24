from django.shortcuts import render, redirect
from reviews.models import Ticket
from reviews.forms import TicketForm

def home(request):
    return render(request, 'reviews/home.html')

def flux(request):
    return render(request, 'reviews/flux.html')

def posts(request):
    return render(request, 'reviews/posts.html')

def subscribed(request):
    return render(request, 'reviews/subscribed.html')


def create_ticket(request):
    ticket_form = TicketForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()

    return render(request, 
            'reviews/create_ticket.html',
            context = {'ticket_form': ticket_form})

def create_review(request):
    pass

def follow_user(request):
    pass

def unfollow_user(request):
    pass

