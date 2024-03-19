from django.contrib import redirect,render
from django.http import HttpResponse
from myApp.models import *

def signupPage(request):
    return render(request,'signup.html')
def logoutPage(request):
    return render(request,'loginPage')
def loginPage(request):
    return render(request,'login.html')
def dashboardPage(request):
    return render(request,'')