from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def index(request):
    return render(request, 'blog/index.html')

def portfolio(request):
    return render(request, 'blog/portfolio.html')

def blog(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/blog.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html')

