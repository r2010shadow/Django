from django.shortcuts import render,redirect
from . import models
from . import forms

def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):

    if request.method == 'POST':
        # username = request.POST.get('username')
        # password = request.POST.get('password')

        login_form = forms.UserForm(request.POST)
        message = 'Open Sesome ! '

        if login_form.is_valid():     # if username.strip() and password:# 确保用户名和密码都不为空
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:        #验证用户名和密码
                user = models.User.objects.get(name = username)
            except:
                message = 'USER in the air'
                return render(request, 'login/login.html',locals())  #返回当前所有的本地变量字典 {'message':message})
            if user.password == password:                            #也可能往模板传入了一些多余的变量数据，造成数据冗余降低效率
                print('[Air]: ', username, password)
                return redirect('/index/')
            else:
                message = 'PASSWORD in the air!'
                return render(request, 'login/login.html', locals()) #{'message': message})
        else:
            return render(request, 'login/login.html', locals())  #{'message': message})

    login_form = forms.UserForm()
    return render(request, 'login/login.html', {'login_form':login_form})     # 或新增 locals()


def register(request):
    pass
    return render(request, 'login/register.html')


def logout(request):
    pass
    return redirect("/login/")