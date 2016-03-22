from django.shortcuts import render
from django.utils import timezone
from .models import Post

def index(request):
    return render(request, 'blog/index.html')

def portfolio(request):
    return render(request, 'blog/portfolio.html')

def blog(request):
    return render(request, 'blog/blog.html')

def about(request):
    return render(request, 'blog/about.html')
