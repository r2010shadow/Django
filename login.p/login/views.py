from django.shortcuts import render, redirect
from . import models
from . import forms
import hashlib
import datetime
from django.conf import settings



def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'login/confirm.html', locals())

    c_time = confirm.c_time
    now = datetime.datetime.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册!'
        return render(request, 'login/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认，请使用账户登录！'
        return render(request, 'login/confirm.html', locals())



def send_email(email, code):

    from django.core.mail import EmailMultiAlternatives

    subject = '来自本案的注册确认邮件'

    text_content = '''自述文本！'''

    html_content = '''
                    <p>注册了么<a href="http://{}/confirm/?code={}" target=blank>www.baidu.com</a>，\
                    这里是本案</p>
                    <p>请点击链接完成注册确认！</p>
                    <p>此链接有效期为{}天！</p>
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    models.ConfirmString.objects.create(code=code, user=user,)
    return code

def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def index(request):
    # pass
    if not request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/login/')
    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login', None):   # 不允许重复登录
        return redirect('/index/')

    if request.method == 'POST':
        # username = request.POST.get('username')
        # password = request.POST.get('password')

        login_form = forms.UserForm(request.POST)
        message = 'Open Sesome ! '

        if login_form.is_valid():  # if username.strip() and password:# 确保用户名和密码都不为空
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            # 用户名字符合法性验证
            # 密码长度验证
            # 更多的其它验证.....
            try:  # 验证用户名和密码
                user = models.User.objects.get(name=username)
            except:
                message = 'USER in the air'
                return render(request, 'login/login.html', locals())  # 返回当前所有的本地变量字典 {'message':message})
                                                                     # 也可能往模板传入了一些多余的变量数据，造成数据冗余降低效率

            if not user.has_confirmed:
                message = '该用户还未经过邮件确认！'
                return render(request, 'login/login.html', locals())


            if user.password == hash_code(password):
                print('[Air]: ', username, password)

                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name

                return redirect('/index/')
            else:
                message = 'PASSWORD in the air!'
                return render(request, 'login/login.html', locals())  # {'message': message})
        else:
            return render(request, 'login/login.html', locals())  # {'message': message})

    login_form = forms.UserForm()
    return render(request, 'login/login.html', {'login_form': login_form})  # 或新增 locals()


def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')

            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'login/register.html', locals())

                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                code = make_confirm_string(new_user)
                send_email(email, code)

                return redirect('/login/')
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")

    request.session.flush()
# 或者使用下面的方法
# del request.session['is_login']
# del request.session['user_id']
# del request.session['user_name']
    return redirect("/login/")
