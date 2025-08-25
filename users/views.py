from django.shortcuts import render

# Create your views here.
def home(request):
    if request.POST:
        form = UserForm(request.POST)
        if form.is_vaild():
        user = form.save()
        return redirect("user:home" user.id)
    else:
        blogs = Blog.objects.order_by()
        return render(request, 'users/home.html', {"blogs": blogs},)