from django.shortcuts import redirect, render
from django.http import HttpResponse
from myApp.models import *

def signupPage(request):
    if request.method == "POST":
        user_name = request.POST.get('username')
        displayname = request.POST.get('display_name')
        mail = request.POST.get('email')
        pass_word=request.POST.get('password')
        usertype=request.POST.get('user_type')

        user = Custom_User.objects.create_user(username=user_name,password=pass_word)
        
        user.dispaly_name=displayname
        user.email=mail
        user.user_type=usertype
        user.save()
    return render(request,'signup.html')
def logoutPage(request):
    return render(request,'loginPage')
def loginPage(request):
    return render(request,'login.html')
def dashboardPage(request):
    user = request.user
    if user.is_authenticated:
        if user.User_type == 'recruiter':
            Template_name = 'Recruiter/dashboard.html'
        elif user.User_type == 'jobseeker':
            Template_name ='JobSeeker/dashboard.html'
        else:
            return HttpResponse("Invalid User")
    else:
        return HttpResponse("User is not authenticated")
    return render(request,Template_name)