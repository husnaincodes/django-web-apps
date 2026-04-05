from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from Home.models import Contact

@login_required(login_url='login')
def index(request):
    return render(request, "project1.html")

@login_required(login_url='login')
def about(request):
    return render(request,"about.html")

@login_required(login_url='login')
def project(request):
    return render(request,"projects.html")

@login_required(login_url='login')
def contact(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = Contact(name=name,email=email,message=message,date= datetime.today())
        contact.save()
    return render(request,"contact.html")