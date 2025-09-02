from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserForm


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(
                reverse("user:profile", kwargs={"id": user.id})
            )  # 假設跳轉到個人頁
        else:
            return render(request, "users/register.html", {"form": form})
    else:
        form = UserForm()
        return render(request, "users/register.html", {"form": form})

def home(request):
  form = UserForm()
  return render(request, "users/home.html", {"form": form})