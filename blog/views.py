from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Nick',
        'title': 'First Post',
        'content': 'This is the First Post',
        'date_posted': 'August 27, 1969'
    },
    {
        'author': 'John',
        'title': 'Second Post',
        'content': 'This is the Second Post',
        'date_posted': 'June 2, 1999'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
