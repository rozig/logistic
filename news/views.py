from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.order_by('-Published_Date')
    return render(request, 'news/news.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'news/news_details.html', {'post': post})