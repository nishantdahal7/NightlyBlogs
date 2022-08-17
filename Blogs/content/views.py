
from email import message
from imaplib import _Authenticator
from multiprocessing import context
import re
from django.shortcuts import render, redirect
from content.models import Post
from django.contrib.auth import authenticate, login, logout

from django.forms import ModelForm

from django.contrib.auth.models import User

# Create your views here.



def signUpPage(request):  
    if request.method == 'POST':
        fn = request.POST['fn']
        ln = request.POST['ln']
        em = request.POST['em']
        un = request.POST['un']
        pw = request.POST['pw']
        user = User.objects.create_user(first_name=fn, last_name=ln, email=em, username=un, password=pw)
        user.save()
       

        return redirect('/login')
   
    return render(request, 'signup.html')

def loginPage(request):
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        user = authenticate(request, username=un, password=pw)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('/login')


def home(request):
    posts = Post.objects.all()[:11]
    data = {
        'posts': posts
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    # print(post)
    return render(request, 'posts.html', {'post': post})
