from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout


def acc_login(request):
    error_msg = ''
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect(request.GET.get('next','/kingadmin'))
        else:
            error_msg = '大侠,访问门派名字或口令有错误！'
    return render(request, 'kingadmin/kingadmin_login.html', {'error_msg':error_msg})



def acc_logout(request):
    logout(request)
    return redirect("king_login")


def app_index(request):
    return render(request, 'kingadmin/app_index.html')