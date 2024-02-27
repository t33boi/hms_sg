from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group



# Create your views here.

from hms_main.models import Person

def login_registerView(request):
    return render(request,'login_register.html')

def loginView(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request, user)
        messages.success(request, 'Logged in Successfully')
        return redirect('home')
    else:
        messages.error(request, 'Incorrect username or password')
        return redirect('login_register')
        
        
           

def registerVIew(request):
    
    username = request.POST.get('username')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    
    if password2 == password1:
        try:
            user = Person.objects.create_user(
                username=username,
                email=email,
                password=password1,
                phoneNumber=phone,
                address=address,
            )
            group = Group.objects.get(name='user')
            user.groups.add(group)
            user.save()
            user = authenticate(request,username=username,password=password1)
            login(request,user)
            messages.success(request,'Account Successfully Created!')
            return redirect('home')
        except:     
            messages.error(request,'Username already Exists!')
            return redirect('login_register')
    else:
        messages.error(request,'Passwords don\'t Match!')
    

def logoutView(request):
    logout(request)
    return redirect('home')