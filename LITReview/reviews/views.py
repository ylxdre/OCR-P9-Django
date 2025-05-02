from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from reviews.models import Ticket, Review
from reviews.forms import TicketForm, ReviewForm


@login_required
def home(request):
    tickets = Ticket.objects.all()
    return render(request, 'reviews/home.html', {'tickets': tickets})

@login_required
def flux(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    context = {
        'tickets': tickets,
        'reviews': reviews,
    }
    return render(request, 'reviews/flux.html', context)

@login_required
def posts(request):
    tickets = Ticket.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)
    return render(request,
            'reviews/posts.html', 
            {'tickets': tickets, 'reviews': reviews})

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
@permission_required('review.change_ticket', raise_exception=True)
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
@permission_required('review.onwer', raise_exception=True)
def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('home')

    return render(request, 
            'reviews/ticket_delete.html',
            {'ticket': ticket})

@login_required
def review(request, review_id):
    review = Review.objects.get(id=review_id)
    ticket = review.ticket
    return render(request,
                  'reviews/review.html',
                  {'review': review})

@login_required
def create_review(request):
    ticket_form = TicketForm()
    review_form = ReviewForm()
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, request.FILES)
        review_form = ReviewForm(request.POST)
        print(request.POST)

        if all([ticket_form.is_valid(), review_form.is_valid()]):
                ticket = ticket_form.save(commit=False)
                print(ticket)
                ticket.user = request.user
                ticket.save()
                review = review_form.save(commit=False)
                print(review)
                review.user = request.user
                review.ticket = ticket
                review.save()
                return redirect('posts')

    context = {
            'ticket_form': ticket_form,
            'review_form': review_form,
            }
    return render(request, 
            'reviews/review_create.html', context)

@login_required
def ticket_review(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    review_form = ReviewForm()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        print(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('posts')
    context = {
            'ticket': ticket,
            'review_form': review_form,
            }
    return render(request,
            'reviews/review_ticket.html', context)


@login_required
def update_review(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        print(request.POST)
        review_form = ReviewForm(request.POST, instance=review)
        print(review_form.is_valid())
        if review_form.is_valid():
            review = review_form.save()
            return redirect('home')
    else:
        review_form = ReviewForm(instance=review)

    return render(request,
                  'reviews/review_update.html',
                  {'review_form': review_form, 'review': review})

@login_required
@permission_required('review.owner', raise_exception=True)
def delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('posts')
    return render(request,
                  'reviews/review_delete.html',
                  {'review': review})

def follow_user(request):
    pass

def unfollow_user(request):
    pass

def delete_confirm(request, truc_id):
    render (request, 
        'reviews/delete_confirm.html')
