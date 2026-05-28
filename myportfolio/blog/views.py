from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import Post
# Create your views here.

import re

def check_input(func):
    def wrapper(request:HttpRequest, *args, **kwargs):
        if request.method == "POST":
            title = request.POST.get("title") or request.POST.get("update_title")
            content = request.POST.get("content") or request.POST.get("update_content")

            if not title or not content:
                return func(request, *args, **kwargs)

            # check the title already present or not if present then then return alert to user and not save the post
            if Post.objects.filter(title=title).exists():
                alert:str = "duplicate"
                context:dict = {
                    "alert" : alert
                }
                return render(request, 'blog/add_post.html', context)

        return func(request, *args, **kwargs)
    return wrapper





def home(request:HttpRequest):
    alert:str = ""
    posts:object = None
    if request.method == "GET":
        posts = Post.objects.all()
        if not posts:
            alert = "null"
    context:dict = {
        "posts": posts,
        "alert" : alert
    }
    return render(request, 'blog/blog_home.html', context)


@check_input
def add_post(request:HttpRequest):
    alert:str = ""
    post:object = None
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if title and content:
            post = Post.objects.create(title=title, content=content)
            return redirect('home')
        else:
            alert = "error"
    context:dict = {
        "post": post,
        "alert" : alert
    }
    return render(request, 'blog/add_post.html', context)

def delete_post(request:HttpRequest, id:int):
    post:object = Post.objects.get(id=id)
    post.delete()
    return redirect('home')

def update_post(request:HttpRequest, id:int):
    alert:str = ""
    post:object = Post.objects.get(id=id)

    if request.method == "POST":
        title = request.POST.get("update_title")
        content = request.POST.get("update_content")

        if title and content:
            post.title = title
            post.content = content
            post.save()
            return redirect('home')
        else:
            alert = "error"
        
    context:dict = {
        "post": post,
        "alert" : alert
    }
    return render(request, 'blog/update_post.html', context)