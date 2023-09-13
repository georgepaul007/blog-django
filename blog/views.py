from django.shortcuts import render, get_object_or_404
from .models import Post, Tag, Author

# Create your views here.

def home_page(request):
    latest_posts = Post.objects.all()[:3]
    print(latest_posts)
    return render(request, "blog/index.html", {
        "posts": latest_posts
    }) 

def posts_page(request):
    all_posts = Post.objects.all()
    print(all_posts)
    return render(request, "blog/posts.html", {
        "all_posts": all_posts
    })

def post_details(request, post):
    slug_post = get_object_or_404(Post, post=post)
    return render(request, "blog/post.html", {
        "post": slug_post
    })