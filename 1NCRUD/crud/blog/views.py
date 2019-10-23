from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import BlogForm
from .models import Blog
from django.views.generic.base import TemplateView

# Create your views here.

#상속할 페이지
def layout(request):
    return render(request, 'blog/layout.html')

#Create
def blogform(request, blog=None):
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
        return render(request, 'blog/new.html', {'form':form})

#Read
def home(request):
    blogs = Blog.objects
    return render(request, 'blog/home.html', {'blogs':blogs})

#Update
def edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return blogform(request, blog)

#Delete
def remove(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('home')

#1:N

