
from django.shortcuts import render
from content.models import Post

# Create your views here.


def home(request):
    posts = Post.objects.all()[:11]
    data = {
        'posts': posts
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    print(post)
    return render(request, 'posts.html', {'post': post})
