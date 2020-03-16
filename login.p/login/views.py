from django.shortcuts import render,redirect
from . import models

def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        message = 'Open Sesome ! '
        if username.strip() and password:# 确保用户名和密码都不为空
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:        #验证用户名和密码
                user = models.User.objects.get(name = username)
            except:
                message = 'USERNAME in the air'
                return render(request, 'login/login.html',{'message':message})
            if user.password == password:
                print('[CAUTION]: ', username, password)
                return redirect('/index/')
            else:
                message = 'PASSWORD in the air!'
                return render(request, 'login/login.html',{'message': message})
        else:
            return render(request, 'login/login.html', {'message': message})
    return render(request, 'login/login.html')


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect("/login/")