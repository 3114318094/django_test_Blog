from django.shortcuts import render, get_object_or_404

# Create your views here.
from Blog.models import Post


def blog_title(request):
    posts_title = Post.objects.all()
    return render(request, 'blog/titles.html', {'blogs': posts_title})


def blog_detail(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detail.html', {'post': post})
