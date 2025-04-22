from django.shortcuts import render

def home(request):
    return render(request, 'reviews/home.html')

def flux(request):
    return render(request, 'reviews/flux.html')

def posts(request):
    return render(request, 'reviews/posts.html')

def subscribed(request):
    return render(request, 'reviews/subscribed.html')


