from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import BlogForm


# Create your views here.

def home(request):
  if request.POST:
    form = BlogForm(request.POST)
    if form.is_valid():
      blog = form.save()
      return redirect("blogs:show", blog.id)
  else:
    blogs = Blog.objects.order_by("-id")
    return render(
      request, "blogs/home.html", {"blogs": blogs},
    )

def show(request, id):
  blog = get_object_or_404(Blog, pk=id)
  if request.POST:
    form = BlogForm(request.POST, instance=blog)
    if form.is_valid():
      form.save()
      return render(request, "blogs/show.html", {"blog": blog})
  else:
    return render(
      request,
      "blogs/show.html", {"blog": blog},
    )

def new(request):
  if request.POST:
    form = BlogForm(request.POST)
    if form.is_valid():
      blog = form.save(commit=False)
      blog.author = request.user
      blog.save()
      return redirect("blogs:home")
  else:
    form = BlogForm()
  return render(request, "blogs/new.html", {"form": form})

def edit(request, id):
  blog = get_object_or_404(Blog, pk=id)

  if request.POST:
    form = BlogForm(request.POST, instance=blog) 
    if form.is_valid():
      form.save()
      return redirect("blogs:show", blog.id)
  else:
    form = BlogForm(instance=blog)

  return render(request, "blogs/edit.html", {"blog": blog, "form": form})

def delete(reuquest, id):
  blog = get_object_or_404(Blog, pk=id)
  blog.delete()

  return redirect("blogs:home")