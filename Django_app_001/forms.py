#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/12/8 20:52
# @Author: max liu
# @File  : forms.py


# Django form field types
# https://www.webforefront.com/django/formfieldtypesandvalidation.html

from django import forms
from django.core.validators import RegexValidator
from Django_app_001.models import OPRS_DEVICE_Base, OPRS_DEVICE_Extension, OPRS_DEVICE_CPU_utli, \
    OPRS_DEVICE_Memory_utli, OPRS_DEVICE_Tips


class StudentsForm(forms.Form):
    # 为了添加必选项前面的星号
    # 下面是模板内的内容
    """
    < style type = "text/css" >
    label.required::before
    {
        content: "*";
    color: red;
    }
    < / style >
    """
    required_css_class = 'required'  # 这是Form.required_css_class属性, use to add class attributes to required rows
    # 添加效果如下
    # <label class="required" for="id_name">学员姓名:</label>
    # 不添加效果如下
    # <label for="id_name">学员姓名:</label>

    # 学员姓名,最小长度2,最大长度10,
    # label后面填写的内容,在表单中显示为名字,
    # 必选(required=True其实是默认值)
    # attrs={"class": "form-control"} 主要作用是style it in Bootstrap
    name = forms.CharField(max_length=10,
                           min_length=2,
                           label='学员姓名',
                           # required=True,
                           widget=forms.TextInput(attrs={'class': "form-control"}))
    # 对电话号码进行校验,校验以1开头的11位数字
    phone_regex = RegexValidator(regex=r'^1\d{10}$',
                                 message="手机号码需要使用11位数字, 例如:'13911153335'")  # 自定义校验方法
    phone_number = forms.CharField(validators=[phone_regex],
                                   min_length=11,
                                   max_length=11,
                                   label='手机号码',
                                   required=True,
                                   widget=forms.NumberInput(attrs={"class": "form-control"}))
    qq_regex = RegexValidator(regex=r'^\d{5,20}$',
                              message="QQ号码需要使用5到20位数字, 例如:'605658506'")
    qq_number = forms.CharField(validators=[qq_regex],
                                min_length=5,
                                max_length=20,
                                label='QQ号码',
                                required=True,
                                widget=forms.NumberInput(attrs={"class": "form-control"}))
    mail = forms.EmailField(required=False,
                            label='学员邮件',
                            widget=forms.EmailInput(attrs={'class': "form-control"}))  # form 输入框类型浏览器自带，包含部分校验

    direction_choices = (('安全', '安全'), ('教主VIP', '教主VIP'))
    direction = forms.CharField(max_length=10,
                                label='学习方向',
                                widget=forms.Select(choices=direction_choices,
                                                    attrs={"class": "form-control"}))

    class_adviser_choices = (('小雪', '小雪'), ('菲儿', '菲儿'))
    class_adviser = forms.CharField(max_length=10,
                                    label='班主任',
                                    widget=forms.Select(choices=class_adviser_choices,
                                                        attrs={"class": "form-control"}))

    payed_choices = ((True, '已缴费'), (False, '未交费'))
    payed = forms.BooleanField(label='缴费情况',
                               required=False,
                               widget=forms.Select(choices=payed_choices,
                                                   attrs={"class": "form-control"}))

    # 需要调用后台数据或更复杂的逻辑校验 ，单独定义表单值得校验函数

    def clean_phone_number(self):  # 对电话号码的唯一性进行校验,注意格式为clean+校验变量
        phone_number = self.cleaned_data['phone_number']  # 提取客户输入的电话号码
        # 在数据库中查找是否存在这个电话号
        # 如果存在就显示校验错误信息
        if StudentsDB.objects.filter(phone_number=phone_number):
            raise forms.ValidationError("电话号码已经存在")  # 抛出表单的错误提示
        # 如果校验成功就返回电话号码
        return phone_number

    def clean_qq_number(self):
        qq_number = self.cleaned_data['qq_number']
        if StudentsDB.objects.filter(qq_number=qq_number):
            raise forms.ValidationError("QQ号码已经存在")
        return qq_number

    def clean_mail(self):
        student_mail = self.cleaned_data.get('mail')
        if StudentsDB.objects.filter(mail=student_mail):
            raise forms.ValidationError('邮件已经存在!')
        return student_mail


class EditStudents(forms.Form):
    required_css_class = 'required'

    student_id = forms.CharField(label='学员唯一ID',
                                 widget=forms.TextInput(attrs={'class': "form-control", 'readonly': True}))

    name = forms.CharField(max_length=10,
                           min_length=2,
                           label='学员姓名',
                           # required=True,
                           widget=forms.TextInput(attrs={'class': "form-control"}))

    # 对电话号码进行校验,校验以1开头的11位数字
    phone_regex = RegexValidator(regex=r'^1\d{10}$',
                                 message="手机号码需要使用11位数字, 例如:'13911153335'")
    phone_number = forms.CharField(validators=[phone_regex],
                                   min_length=11,
                                   max_length=11,
                                   label='手机号码',
                                   required=True,
                                   widget=forms.NumberInput(attrs={"class": "form-control"}))
    qq_regex = RegexValidator(regex=r'^\d{5,20}$',
                              message="QQ号码需要使用5到20位数字, 例如:'605658506'")
    qq_number = forms.CharField(validators=[qq_regex],
                                min_length=5,
                                max_length=20,
                                label='QQ号码',
                                required=True,
                                widget=forms.NumberInput(attrs={"class": "form-control"}))

    mail = forms.EmailField(required=False,
                            label='学员邮件',
                            widget=forms.EmailInput(attrs={'class': "form-control"}))

    direction_choices = (('安全', '安全'), ('教主VIP', '教主VIP'))
    direction = forms.CharField(max_length=10,
                                label='学习方向',
                                widget=forms.Select(choices=direction_choices,
                                                    attrs={"class": "form-control"}))

    class_adviser_choices = (('小雪', '小雪'), ('菲儿', '菲儿'))
    class_adviser = forms.CharField(max_length=10,
                                    label='班主任',
                                    widget=forms.Select(choices=class_adviser_choices,
                                                        attrs={"class": "form-control"}))

    payed_choices = ((True, '已缴费'), (False, '未交费'))
    payed = forms.BooleanField(label='缴费情况',
                               required=False,
                               widget=forms.Select(choices=payed_choices,
                                                   attrs={"class": "form-control"}))

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        stu_id = self.cleaned_data.get('student_id')
        # 在编辑的时候,校验电话号码与创建不同,因为其实数据库里边已经有一个自己这个条目的电话号码了!
        # 所以要排除自己ID查到的电话号码,如果其他ID依然存在相同的电话号码,就校验失败
        count = 0
        for i in StudentsDB.objects.filter(phone_number=phone_number):
            if int(i.id) != int(stu_id):
                count += 1

        if count >= 1:
            raise forms.ValidationError("电话号码已经存在")
        return phone_number

    def clean_qq_number(self):
        qq_number = self.cleaned_data['qq_number']
        stu_id = self.cleaned_data.get('student_id')
        count = 0
        for i in StudentsDB.objects.filter(qq_number=qq_number):
            if int(i.id) != int(stu_id):
                count += 1

        if count >= 1:
            raise forms.ValidationError("QQ号码已经存在")
        return qq_number

    def clean_mail(self):
        student_mail = self.cleaned_data.get('mail')
        stu_id = self.cleaned_data.get('student_id')
        student_obj = StudentsDB.objects.filter(mail=student_mail)
        for student in student_obj:
            if student.id != int(stu_id):
                raise forms.ValidationError('邮件已经被其他学员使用!')
        return student_mail


class UserForm(forms.Form):
    username = forms.CharField(label='用户名',
                               max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "用户名"})
                               )
    password = forms.CharField(label='密码',
                               max_length=100,
                               required=True,
                               widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "密码"})
                               )


#####################################################################################################################
# 添加设备的表单

class Device_infor(forms.Form):
    # 必填表单前* 调用js
    required_css_class = 'required'

    device_name = forms.CharField(max_length=50,
                                  required=True,
                                  label='设备名',
                                  widget=forms.TextInput(attrs={'class': "form-control"})
                                  )

    device_nas_ip = forms.GenericIPAddressField(required=True,
                                                label='设备管理地址',
                                                widget=forms.TextInput(
                                                    attrs={'class': "form-control", "placeholder": "ipv4 or ipv6:"})
                                                )

    device_module = forms.CharField(max_length=50,
                                    required=True,
                                    label='设备型号',
                                    widget=forms.TextInput(attrs={'class': "form-control"})
                                    )

    type_choices = (
        ('router', '路由器'), ('switch', '交换机'), ('firewall', '防火墙'), ('other', '其他'))  # 表单约束，只能选择给定，和数据库表值约束匹配
    device_type = forms.CharField(required=True,
                                  label='设备类型',
                                  widget=forms.Select(choices=type_choices, attrs={'class': "form-control"})
                                  )

    Vendor_choices = (
        ('Cisco', '思科'), ('Juniper', '瞻博'), ('H3C', '华三'), ('HUAWEI', '华为'), ('other', '其他'))  # 表单约束，只能选择给定，和数据库表值约束匹配
    Vendor = forms.CharField(required=True,
                             label='设备厂商',
                             widget=forms.Select(choices=Vendor_choices, attrs={'class': "form-control"})
                             )

    sn_regex = RegexValidator(regex=r'^\S*$',
                              message="SN must be ....不包含空字符")  # 校验失败的消息会通过form.errow推送
    device_sn = forms.CharField(validators=[sn_regex],
                                max_length=11,
                                min_length=11,
                                required=True,
                                label='设备SN',
                                widget=forms.TextInput(
                                    attrs={'class': "form-control", "placeholder": "11位设备SN"})
                                )

    # mail = forms.EmailField(required=False,
    #                         label='厂家联系邮件',
    #                         widget=forms.EmailInput(attrs={'class': "form-control"})
    #                         )

    tips = forms.CharField(required=False,
                           label='备注',
                           widget=forms.Textarea(attrs={'class': "form-control"}))

    def clean_device_name(self):  # 调用字段的clean函数 并实例化该对象，只能取该字段的值，无法去其他字段值
        device_name = self.cleaned_data.get('device_name')
        print(device_name)
        if OPRS_DEVICE_Base.objects.filter(device_name=device_name).exists():
            raise forms.ValidationError('name已存在4！')  # 抛出异常到form.errow 类
        return device_name

    def clean_device_sn(self):
        device_sn = self.cleaned_data.get('device_sn')
        if OPRS_DEVICE_Base.objects.filter(device_sn=device_sn):
            raise forms.ValidationError('SN已存在5！')
        return device_sn

    def clean_device_nas_ip(self):
        device_nas_ip = self.cleaned_data.get('device_nas_ip')
        if OPRS_DEVICE_Extension.objects.filter(device_nas_ip=device_nas_ip):
            raise forms.ValidationError('ip已存在6！')
        return device_nas_ip


# update的表单

class Device_update(forms.Form):
    # 必填表单前* 调用js
    required_css_class = 'required'

    device_id = forms.IntegerField(label='设备唯一ID',
                                   widget=forms.NumberInput(attrs={'class': "form-control", 'readonly': True}))

    device_name = forms.CharField(max_length=50,
                                  required=True,
                                  label='设备名',
                                  widget=forms.TextInput(attrs={'class': "form-control"})
                                  )

    sn_regex = RegexValidator(regex=r'^\S*$',
                              message="SN must be ....")  # 校验失败的消息会通过form.error推送
    device_sn = forms.CharField(validators=[sn_regex],
                                max_length=11,
                                min_length=11,
                                required=True,
                                label='设备SN',
                                widget=forms.TextInput(
                                    attrs={'class': "form-control", "placeholder": "11位设备SN"})
                                )

    device_ip = forms.GenericIPAddressField(required=True,
                                            label='设备管理地址',
                                            widget=forms.TextInput(
                                                attrs={'class': "form-control", "placeholder": "ipv4 or ipv6:"})
                                            )

    mail = forms.EmailField(required=False,
                            label='厂家联系邮件',
                            widget=forms.EmailInput(attrs={'class': "form-control"})
                            )

    direction_choices = (('router', '路由器'), ('switch', '交换机'))  # 表单约束，只能选择给定，和数据库表值约束匹配
    device_type = forms.CharField(required=True,
                                  label='设备类型',
                                  widget=forms.Select(choices=direction_choices, attrs={'class': "form-control"})
                                  )

    op_choices = ((True, '已纳管'), (False, '未纳管'))
    device_op = forms.BooleanField(required=False,
                                   label='是否纳管',
                                   widget=forms.Select(choices=op_choices, attrs={'class': "form-control"})
                                   )

    tips = forms.CharField(required=False,
                           label='备注',
                           widget=forms.Textarea(attrs={'class': "form-control"}))

    #  不能更新为其他已存在的条目内容
    def clean_device_name(self):
        device_name = self.cleaned_data.get('device_name')
        device_id = self.cleaned_data.get('device_id')
        if [item for item in OPRS_DEVICE_Base.objects.filter(device_name=device_name) if
            item.id != int(device_id)]:  # if为false，即查不到信息时，不一定完全正确，可能是一个已被删除的设备，最终判断交给view device_update主函数
            raise forms.ValidationError('name已存在1！')  # 抛出异常到form.error 类
        return device_name

    def clean_device_sn(self):
        device_sn = self.cleaned_data.get('device_sn')
        device_id = self.cleaned_data.get('device_id')
        if [item for item in OPRS_DEVICE_Base.objects.filter(device_sn=device_sn) if item.id != int(device_id)]:
            raise forms.ValidationError('SN已存在2！')
        return device_sn

    def clean_device_ip(self):
        device_ip = self.cleaned_data.get('device_ip')
        device_id = self.cleaned_data.get('device_id')
        print(device_id)
        print(type(device_id))
        if [item for item in OPRS_DEVICE_Base.objects.filter(device_ip=device_ip) if item.id != int(device_id)]:
            raise forms.ValidationError('ip已存在3！')
        return device_ip


class UserForm(forms.Form):
    username = forms.CharField(label=False,
                               max_length=10,
                               required=True,
                               widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Username: t1"})
                               )
    password = forms.CharField(label=False,
                               max_length=100,
                               required=True,
                               widget=forms.PasswordInput(
                                   attrs={"class": "form-control", "placeholder": "Password: t12345678"})
                               )
