from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from Django_app_001.forms import Device_infor, Device_update
from Django_app_001.models import OPRS_DB, CPU_memory_utli
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
# 此permission_required仅仅是操作URL的函数的权限，没有则默认重定向到主页（ajax内的URL对应函数没有权限则会获取不到数据，承载的主页没有对应ajax数据），具体是否能操作数据库取决于后台真正的用户权限


@login_required()
def index_go(request):
    title_value = '人生苦短，我用python'
    body_value = '哈哈哈哈啊哈哈哈'
    return render(request, 'index.html', {'return_title': title_value, 'reutrn_body': body_value})


# @permission_required('Django_app_001.add_oprs_db')
@login_required()
def device_add(request):
    if request.method == 'GET':
        form = Device_infor()
        return render(request, 'device_add.html', {'form': form})
    elif request.method == 'POST':
        form_post = Device_infor(request.POST)  # 包含POST数据的form，非空表单

        # A Form instance has an is_valid() method, which runs validation routines for all its fields. When this method is called, if all fields contain valid data, it will:
        #
        # return True
        # place the form’s data in its cleaned_data attribute.
        if form_post.is_valid():  # 调用clear函数去后台检查约束条件，有两个动作去执行
            oprs_add = OPRS_DB(device_name=request.POST.get('device_name'),
                               device_sn=request.POST.get('device_sn'),
                               device_ip=request.POST.get('device_ip'),
                               mail=request.POST.get('mail'),
                               device_type=request.POST.get('device_type'),
                               device_op=request.POST.get('device_op'),
                               tips=request.POST.get('tips'),
                               )
            oprs_add.save()
            form = Device_infor()
            return render(request, 'device_add.html', {'form': form, 'successmessage': '设备添加完成!'})
        else:
            return render(request, 'device_add.html', {'form': form_post})  # 如果clear函数后台校验不通过，则把数据原封不动返回


# @permission_required('Django_app_001.view_oprs_db')
@login_required()
def device_select(request, successmessage=None, errormessage=None):
    db_infor = OPRS_DB.objects.all()
    db_all = [
        {'device_id': item.id,
         'device_name': item.device_name,
         'device_sn': item.device_sn,
         'device_ip': item.device_ip,
         'mail': item.mail,
         'device_type': item.device_type,
         'device_op': item.device_op,
         'create_date': item.create_date.strftime("%Y-%m-%d %H:%M:%S"),
         'update_date': item.update_date.strftime("%Y-%m-%d %H:%M:%S"),
         'tips': item.tips,
         'device_del': '/device_del/' + str(item.id),
         'device_update': '/device_update/' + str(item.id)} for item in db_infor]
    print(db_all)
    return render(request, 'device_select.html',
                  {'db_all': db_all, 'successmessage': successmessage, 'errormessage': errormessage})


# @permission_required('Django_app_001.view_oprs_db')
# @permission_required('Django_app_001.delete_oprs_db')
@login_required()
def device_del(request, device_id):
    try:
        del_item = OPRS_DB.objects.get(id=device_id)
        del_item.delete()
        return device_select(request, successmessage='删除成功！')
    except OPRS_DB.DoesNotExist:
        return device_select(request, errormessage='此设备不存在或已被删除！')


# @permission_required('Django_app_001.change_oprs_db')
@login_required()
def device_update(request, device_id):
    if request.method == 'GET':
        try:  # 多人操作时，在查询界面上，A删除后，B没有刷新页面，编辑不存在的设备时 DoesNotExist的捕获
            item = OPRS_DB.objects.get(id=device_id)
            tt = OPRS_DB.objects.filter(id=device_id)
            init_form = Device_update(initial={
                'device_id': item.id,
                'device_name': item.device_name,
                'device_sn': item.device_sn,
                'device_ip': item.device_ip,
                'mail': item.mail,
                'device_type': item.device_type,
                'device_op': item.device_op,
                'tips': item.tips
            })

            return render(request, 'device_update.html', {'form': init_form})
        except OPRS_DB.DoesNotExist:
            return device_select(request, errormessage='此设备不存在或已被删除！')

    elif request.method == 'POST':
        form_post = Device_update(request.POST)  # 包含POST数据的form，非空表单
        if form_post.is_valid():
            try:  # 多人操作时，在update界面上 ，A删除后，B没有刷新页面，更新不存在的设备时 DoesNotExist的捕获
                item = OPRS_DB.objects.get(id=device_id)
                item.device_name = request.POST.get('device_name')
                item.device_sn = request.POST.get('device_sn')
                item.device_ip = request.POST.get('device_ip')
                item.mail = request.POST.get('mail')
                item.device_type = request.POST.get('device_type')
                item.device_op = request.POST.get('device_op')
                item.tips = request.POST.get('tips')
                item.save()

                return device_select(request, successmessage='更新成功！')
            except OPRS_DB.DoesNotExist:
                return device_select(request, errormessage='此设备不存在或已被删除！')
        else:
            return render(request, 'device_update.html', {'form': form_post})


# @permission_required('Django_app_001.view_cpu_memory_utli')
@login_required()
def chartjs_from_django(request):
    items = CPU_memory_utli.objects.filter(device_ip='172.1.1.1')
    labelname = ['CPU利用率', 'Memory利用率']
    cpu_values = []
    memory_values = []
    device_name_list = []
    device_ip_list = []
    monitor_time = []
    for item in items:
        device_name_list.append(item.device_name)
        device_ip_list.append(item.device_ip)
        cpu_values.append(item.cpu_utli)
        memory_values.append(item.memory_utli)
        monitor_time.append(item.create_date.strftime("%Y-%m-%d %H:%M:%S"))

    print(labelname)
    print(monitor_time)
    print(cpu_values, memory_values)
    print(device_name_list[0])
    print(device_ip_list[0])
    return render(request, 'chartjs_from_django.html', {'labelname': json.dumps(labelname),
                                                        'x_values': json.dumps(monitor_time),
                                                        'y_values': json.dumps([cpu_values, memory_values]),
                                                        'title': device_name_list[0] + '/' + device_ip_list[0]})


@login_required()
def chartjs_from_ajax(request):
    return render(request, 'chartjs_from_ajax.html')


@login_required()
def echarts_from_django(request):
    return 'pass'


@login_required()
def echarts_from_ajax(request):
    return 'pass'
