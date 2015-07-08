from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout,login as djando_login, authenticate

#-*- coding: utf-8 -*-
# Create your views here.
def login(request):
    error_messages=[]
    if request.method == 'POST':
        username = request.POST['usr']
        password = request.POST['pwd']
        user = authenticate(username=username, password=password)
        if user is None:
            error_messages.append('Nombre de usuario o contraseña incorrecto')
        else:
            if user.is_active:
                djando_login(request,user)
                return redirect('photos_home')
            else:
                error_messages.append('El usuario no esta activo')
    context = {
        'errors': error_messages
    }
    return render(request,'users/login.html',context)

def logout(request):
    if request.user.is_authenticated():
        django_logout(request)
    return redirect ('photos_home')