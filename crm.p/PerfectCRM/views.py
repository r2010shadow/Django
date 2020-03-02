from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

def acc_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect('/crm/')
    return render(request, 'login.html')


def acc_logout(request):
    logout(request)
    return redirect("/login/")