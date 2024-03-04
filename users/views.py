from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    form = RegisterForm() #Crea formulario vacio
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid(): 
            form.save()
            messages.success(request, "Su cuenta ha sido creada de forma exitosa")
            return redirect("signin")
        
    context = {"form":form}
    return render(request, "users/signup.html", context)


def signin(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        
        else:
            messages.warning(request, "Credenciales incorrectas. Por favor, intentálo otra vez")
            return redirect("signin")
        
    context = {}
    return render(request, "users/login.html", context)

def signout(request):
    logout(request)
    return redirect("signin")

"""
@login_required(login_url="signin")
def profile(request):
    user = request.user
    blogs = Blog.objects.filter(user=user)
    context={"user": user, "blogs": blogs}
    return render(request, "core/profile.html", context)

@login_required(login_url="signin")
def update_profile(request):
    if request.user.is_authenticated:
        user = request.user
        form = UpdateProfileForm(instance=user)
        if request.method == 'POST':
            form = UpdateProfileForm(request.POST, request.FILES, instance=user)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated successfully")
                return redirect("profile")
        
        
    context = {"form": form}
    return render(request, "core/update_profile.html", context)

"""