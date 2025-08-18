from django.shortcuts import render

# Create your views here.

app_name = 'pages'

def home(request):
  return render(request, "pages/home.html")

def about(request):
  return render(request, "pages/about.html")