from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile,EmailVerifyRecord
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm
from django.contrib.auth.hashers import make_password
from utils.email_send import send_register_eamil


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))

            if user.check_password(password):
                return user
        except Exception as e:
            return None


def user_login(request):
    if request.method == 'POST':

        user_name = request.POST.get('username', None)
        pass_word = request.POST.get('password', None)

        user = authenticate(username=user_name, password=pass_word)

        if user is not None:

            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})

    elif request.method == 'GET':
        return render(request, 'login.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):

        login_form = LoginForm(request.POST)
        if login_form.is_valid():

            user_name = request.POST.get('username', None)
            pass_word = request.POST.get('password', None)

            user = authenticate(username=user_name, password=pass_word)

            if user is not None:
                if user.is_active:

                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return render(request, 'login.html', {'msg': '用户名或密码错误', 'login_form': login_form})
            else:
                return render(request, 'login.html', {'login_form': login_form})

        else:
            return render(request, 'login.html', {'login_form': login_form})


class RegisterView(View):

    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html',{'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', None)

            if UserProfile.objects.fillter(email = user_name):
                return render(request, 'register.html', {'register_form' : register_form, 'msg': '用户已存在'})

            pass_word = request.POST.get('password', None)
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False

            user_profile.password = make_password(pass_word)
            user_profile.save()
            send_register_eamil(user_name, 'register')
            return render(request, 'login.html')
        else:
            return render(request, 'register.html' ,{'register_form':register_form})






class ActiveUserView(View):
    def get(self, request, active_code):
        # 查询邮箱验证记录是否存在
        all_record = EmailVerifyRecord.objects.filter(code = active_code)

        if all_record:
            for record in all_record:
                # 获取到对应的邮箱
                email = record.email
                # 查找到邮箱对应的user
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
         # 验证码不对的时候跳转到激活失败页面
        else:
            return render(request,'active_fail.html')
        # 激活成功跳转到登录页面
        return render(request, "login.html", )









