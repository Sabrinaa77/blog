from django.shortcuts import render
from .models import Blog

# Create your views here.

def home(request):
  if request.POST:
    form = BlogForm(request.POST)
    return redirect("blogs:show", blogs.id)
  else:
    blogs = Blog.objects.order_by("-id")
    return render(
      request, "blogs/home.html", {"blogs": blogs},
    )
  return render(request, "blogs/home.html")

def show(request):
  blog = get_object_or_404(Blog, pk=id)

  if request.POST:
    form = PostForm(request.POST, instance=blog)
    form.save()
    return render(request, "blogs/show.html", blog.id)
  else:
    return render(
      request,
      "blogs/show.html", {"blog": blog},
    )


def new(request):
  return render(request, "blogs/new.html")