from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Comment

# Create your views here.
def index(request):
    posts = BlogPost.objects.all().order_by('-pub_date')
    return render(request, 'blog_index.html', { 'posts': posts })

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_detail.html', { 'post': post })
