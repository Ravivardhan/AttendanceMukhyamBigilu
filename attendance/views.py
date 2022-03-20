from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
from django.contrib import messages
from django.db import IntegrityError

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.

def index(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        #email=request.POST['email']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"login successful")

            return HttpResponse(f"Welcome\t\t{username}")
        else:
            messages.error(request,'invalid username/password')

            return redirect('/')
    return render(request,'login.html')

def register(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        print(username)
        try:
            if len(password)>=8:
                user = User.objects.create_user(username=str(username), email=str(email), password=password)
                user.save()
                login(request,user)

                return redirect('/')
            else:
                messages.error(request, 'Password must contain atleast 8 characters')

                return redirect('/register')
        except IntegrityError as e:
            messages.error(request, 'username already taken')
            return redirect('/register')

    return render(request,'register.html')