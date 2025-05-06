from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import CharField, Value
from authentication.models import User
from reviews.models import Ticket, Review, UserFollows
from reviews.forms import TicketForm, ReviewForm, ToFollowForm
from itertools import chain


@login_required
def home(request):
    tickets = Ticket.objects.all()
    return render(request,
                  'reviews/home.html',
                  {'tickets': tickets})


@login_required
def flux(request):
    followed = UserFollows.objects.filter(user=request.user)
    users_followed = []
    for userf in followed:
        users_followed.append(userf.followed_user)
    tickets = Ticket.objects.filter(user__in=users_followed)
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = Review.objects.filter(user__in=users_followed)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.time_created,
        reverse=True)
    return render(request,
                  'reviews/flux.html',
                  {'posts': posts})


@login_required
def posts(request):
    tickets = Ticket.objects.filter(user=request.user)
    reviews = Review.objects.filter(user=request.user)
    return render(request,
                  'reviews/posts.html',
                  {'tickets': tickets, 'reviews': reviews})


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
            return redirect('flux')
    return render(request,
                  'reviews/ticket_create.html',
                  context={'ticket_form': ticket_form, 'tickets': tickets})


@login_required
@permission_required('review.change_ticket', raise_exception=True)
def update_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket_form = TicketForm(request.POST, instance=ticket)
        if ticket_form.is_valid():
            ticket = ticket_form.save()
            return redirect('flux')
    else:
        ticket_form = TicketForm(instance=ticket)

    return render(request,
                  'reviews/ticket_update.html',
                  {'ticket_form': ticket_form})


@login_required
@permission_required('review.delete_ticket', raise_exception=True)
def delete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('flux')

    return render(request,
                  'reviews/ticket_delete.html',
                  {'ticket': ticket})


@login_required
def review(request, review_id):
    review = Review.objects.get(id=review_id)
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
            review = review_form.save(commit=False)
            review.user = ticket.user = request.user
            review.save()
            ticket.save()
            review.ticket = ticket
            ticket.review = review
            ticket.save()
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
            ticket.review = review
            review.save()
            ticket.review = review
            ticket.save()
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
            return redirect('posts')
    else:
        review_form = ReviewForm(instance=review)
    return render(request,
                  'reviews/review_update.html',
                  {'review_form': review_form, 'review': review})


@login_required
def delete_review(request, review_id):
    review = Review.objects.get(id=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('posts')
    return render(request,
                  'reviews/review_delete.html',
                  {'review': review})


@login_required
def subscribed(request):
    follows = UserFollows()
    user_form = ToFollowForm()
    following = UserFollows.objects.filter(followed_user=request.user)
    if request.method == 'POST':
        user_form = ToFollowForm(request.POST)
        if user_form.is_valid():
            user = user_form.cleaned_data["user"]
            user_followed = User.objects.filter(username=user)
            follows.followed_user = user_followed[0]
            follows.user = request.user
            follows.save()
            return redirect('subscribed')
    followed = UserFollows.objects.filter(user=request.user)
    context = {
        'user_form': user_form,
        'followed': followed,
        'following': following
    }
    return render(request,
                  'reviews/subscribed.html', context)


@login_required
def unsubscribe(request, followed_user_id):
    followed = UserFollows.objects.get(
        user=request.user,
        followed_user=followed_user_id)
    if request.method == 'POST':
        followed.delete()
        return redirect('subscribed')
    return render(request,
                  'reviews/unsubscribe.html',
                  {'followed': followed})
