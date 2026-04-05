

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.user.is_authenticated:
        return redirect("Home")  # Redirect if already logged in
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        # Use Django's built-in authentication
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect("Home")
        else:
            messages.error(request, "Invalid username or password!")
    
    return render(request, "login.html")

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect("login")
