from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from . import app_setup
from .sites import site
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from kingadmin import form_handle


def acc_login(request):
    error_msg = ''
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(request.GET.get('next', '/kingadmin'))
        else:
            error_msg = '大侠,访问门派名字或口令有错误！'
    return render(request, 'kingadmin/kingadmin_login.html', {'error_msg': error_msg})


def acc_logout(request):
    logout(request)
    return redirect("king_login")


def app_index(request):
    return render(request, 'kingadmin/app_index.html', {'site': site})


app_setup.kingadmin_auto_discover()
print('site', site.enable_admins)


@login_required
def table_obj_list(request, app_name, model_name):
    '''取出指定model里的数据返回给前端'''
    # 拿到admin_class后，通过它找到拿到model
    admin_class = site.enable_admins[app_name][model_name]
    querysets = admin_class.model.objects.all().order_by('-id')
    # 过滤
    querysets, filter_conditions = get_filter_result(request, querysets)
    admin_class.filter_conditions = filter_conditions
    # 分页
    paginator = Paginator(querysets, 2)
    page = request.GET.get('page')
    try:
        querysets = paginator.page(page)
    except PageNotAnInteger:
        querysets = paginator.page(1)
    except EmptyPage:
        querysets = paginator.page(paginator.num_pages)

    return render(request, 'kingadmin/table_obj_list.html',
                  {'querysets': querysets, 'admin_class': admin_class})


def get_filter_result(request, querysets):
    filter_conditions = {}
    for key, val in request.GET.items():
        if key == 'page': continue
        if val:
            filter_conditions[key] = val

    return querysets.filter(**filter_conditions), filter_conditions


@login_required
def table_obj_list(request, app_name, model_name):
    admin_class = site.enable_admins[app_name][model_name]
    querysets = admin_class.model.objects.all()
    querysets, filter_conditions = get_filter_result(request, querysets)
    admin_class.filter_conditions = filter_conditions
    return render(request, 'kingadmin/table_obj_list.html',
                  {'querysets': querysets, 'admin_class': admin_class})


@login_required
def table_obj_change(request, app_name, model_name, obj_id):
    admin_class = site.enable_admins[app_name][model_name]
    model_form = form_handle.create_dynamic_model_form(admin_class)

    # 让表单可修改
    obj = admin_class.model.objects.get(id=obj_id)

    if request.method == 'GET':
        form_obj = model_form(instance=obj)
    elif request.method == 'POST':
        form_obj = model_form(instance=obj, data=request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect("/kindadmin/%s/%s/" % (app_name, model_name))
    return render(request, 'kingadmin/table_obj_change.html', locals())


@login_required
def table_obj_add(request, app_name, model_name):

    admin_class = site.enable_admins[app_name][model_name]
    model_form = form_handle.create_dynamic_model_form(admin_class, form_add=True)

    if request.method == 'GET':
        form_obj = model_form()
    elif request.method == 'POST':
        form_obj = model_form(data=request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect("/kingadmin/%s/%s/"%(app_name, model_name))
    return render(request, 'kingadmin/table_obj_add.html', locals())











