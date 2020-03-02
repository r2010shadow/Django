from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def acc_login(request):
    error_msg = ''
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        #next_url = request.GET.get('next')             https://www.jianshu.com/p/4e896d42b6c3

        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            #if next_url:
            #    return redirect(next_url)
            return redirect('/crm')
            #return redirect(request.GET.get('next','/'))
        else:
            error_msg = '少侠，访问门派名字或口令有错误！'
    return render(request,'login.html',{'error_msg':error_msg})



def acc_logout(request):
    logout(request)
    return redirect("acc_login")