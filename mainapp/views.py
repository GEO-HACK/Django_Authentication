from django.shortcuts import render
from django.contrib.auth.decorators import  login_required

# Create your views here.
@login_required
def dashboard(request):
    return render(request,'registration/dashboard.html', {'section':'dashboard'})

def login(request):
    return render(request,'registration/login.html', {'section':'login'})

def logout(request):
    return render(request,'mainapp/logout.html', {})