from django.shortcuts import render
from student_management_app.EmailBackEnd import EmailBackEnd
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def showDemopage(request):
    return render(request,"demo.html")

def ShowLoginPage(request):
    return render(request,"login_page.html")
from django.http import HttpResponse

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("staff_home"))
            else:
                return HttpResponseRedirect(reverse("student_home"))

        else:
            messages.error(request,"invalid Login Details")
            return HttpResponseRedirect("/")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User : "+request.user.email+" usertype: "+request.user.user_type)
    else:
        return HttpResponse("please Login First")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")


















