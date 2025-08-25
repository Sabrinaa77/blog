from django.contrib.auth import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.


def register(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_vaild():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})
