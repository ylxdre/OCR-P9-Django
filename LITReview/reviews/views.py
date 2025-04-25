from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from reviews.models import Ticket
from reviews.forms import TicketForm

@login_required
def home(request):
    tickets = Ticket.objects.all()
    return render(request, 'reviews/home.html', {'tickets': tickets})

@login_required
def flux(request):
    return render(request, 'reviews/flux.html')

@login_required
def posts(request):
    return render(request, 'reviews/posts.html')

@login_required
def subscribed(request):
    return render(request, 'reviews/subscribed.html')

@login_required
def ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request,
            'reviews/ticket.html',
            {'ticket': ticket})

@login_required
def create_ticket(request):
    tickets = Ticket.objects.all()
    ticket_form = TicketForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    return render(request, 
            'reviews/ticket_create.html',
            context = {'ticket_form': ticket_form, 'tickets': tickets})

@login_required
def update_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, instance=ticket)
        if ticket_form.is_valid():
            ticket = ticket_form.save()
            return redirect('home')
    else:
        ticket_form = TicketForm(instance=ticket)

    return render(request, 
            'reviews/ticket_update.html',
            {'ticket_form': ticket_form})

@login_required
def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('home')

    return render(request, 
            'reviews/ticket_delete.html',
            {'ticket': ticket})

def review(request):
    pass

def create_review(request):
    pass

def update_review(request):
    pass

def delete_review(request):
    pass

def follow_user(request):
    pass

def unfollow_user(request):
    pass

def delete_confirm(request, truc_id):
    render (request, 
        'reviews/delete_confirm.html')
