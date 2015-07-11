from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout,login as djando_login, authenticate
from django.forms import loginForm
#-*- coding: utf-8 -*-
# Create your views here.
def login(request):

    #form = LoginForm()


    error_messages=[]
    if request.method == 'POST':
        username = request.POST['usr']
        password = request.POST['pwd']
        user = authenticate(username=username, password=password)
        if user is None:
            error_messages.append('Nombre de usuario o password incorrecto')
        else:
            if user.is_active:
                djando_login(request,user)
                return redirect('photos_home')
            else:
                error_messages.append('El usuario no esta activo')
    context = {
        'errors': error_messages
        'login_form': form
    }
    return render(request,'users/login.html',context)

def logout(request):
    if request.user.is_authenticated():
        django_logout(request)
    return redirect ('photos_home')