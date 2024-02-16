from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Comment
from .forms import CommentForm

# Create your views here.
def index(request):
    posts = BlogPost.objects.all().order_by('-pub_date')
    return render(request, 'blog_index.html', { 'posts': posts })

def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    comments = Comment.objects.filter(post=post)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog_detail.html', {'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})
