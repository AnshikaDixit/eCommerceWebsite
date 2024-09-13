
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . models import Blogpost

def index(request):
    myPosts = Blogpost.objects.all()
    print(myPosts)
    return render(request, 'blog/index.html', {"myPosts":myPosts})

def blogpost(request, id):
    post = Blogpost.objects.filter(post_id = id)[0]
    print(post)
    return render(request, 'blog/blogpost.html', {"post":post})