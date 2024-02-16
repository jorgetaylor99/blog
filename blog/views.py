from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.
def index(request):
    posts = BlogPost.objects.all().order_by('-pub_date')
    return render(request, 'blog_index.html', {'posts': posts})
    # return HttpResponse("Hello World. You're at the blog index.")
