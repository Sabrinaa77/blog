from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('/', views.home, name='home'),
    path('/new/', views.new, name='new'),
    path('/<int:id>/', views.show, name='show'),
]