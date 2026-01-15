from urllib import request
from urllib.request import Request
from django.shortcuts import render, redirect
from .models import BlogPost

# Create your views here.
def home(request):
    blogs= BlogPost.objects.all()
    return render(request, "home.html", {"blogs": blogs})

def add_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        BlogPost.objects.create(title=title, content=content)
        return redirect("home")
    return render(request, "add_blog.html")

def update_blog(request, blog_id): 
    
    blog = BlogPost.objects.get(id=blog_id) 
 
    if request.method == 'POST': 
        title = request.POST.get('title') 
        content = request.POST.get('content') 
 
        if title and content: 
            blog.title = title 
            blog.content = content 
            blog.save() 
            return redirect('home') 
 
    return render(request, 'update_blog.html', {'blog': blog})

def delete_blog(request, blog_id): 
    blog = BlogPost.objects.get(id=blog_id) 
 
    if request.method == 'POST': 
        blog.delete() 
        return redirect('home') 
    return render(request, 'delete_blog.html', {'blog': blog})