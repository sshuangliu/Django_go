from django.db import models
from django.core.validators import RegexValidator


# python3 manage.py startapp Django_001app  创建子系统APP
# python3 manage.py check
# python3 manage.py makemigrations 生产表脚本文件
# python3 manage.py migrate 产生表操作
# Create your models here.

# Django model data types
# https://www.webforefront.com/django/modeldatatypesandvalidation.html

#

# class Department(models.Model):
#     name = models.CharField(max_length=100, blank=False, null=False)
#     summary = models.CharField(max_length=10000, blank=True, null=True)
#     teacher = models.CharField(max_length=100, blank=False)
#     method = models.CharField(max_length=100, blank=False)
#     characteristic = models.CharField(max_length=100, blank=True, null=True)
#     if_provide_lab = models.BooleanField(default=True)
#     detail = models.CharField(max_length=10000, blank=False)
#
#     # def __str__(self):
#     #     return f"{self.__class__.__name__}(Name: {self.name} | Teacher: {self.teacher})"
#
#
# class StudentsDB(models.Model):
#     name = models.CharField(max_length=100, verbose_name='学员姓名')
#     mail = models.EmailField(max_length=100, unique=True, verbose_name='学员邮件')
#     edit_date = models.DateField(auto_now=True, verbose_name='修改时间')
#
#     def __str__(self):
#         return f"{self.__class__.__name__}(Name: {self.name} | Email: {self.mail})"


# 创建数据库的约束条件: 字段类型本身的约束 自定义的约束，（form表单的约束)

class OPRS_DEVICE_Base(models.Model):
    device_name = models.CharField(blank=False, null=False, max_length=100, verbose_name='设备名', unique=True)
    # SN,校验不包含空类型字符,最大长度为11,不可以为空,唯一键(注意:并没有min_length这个控制字段)
    sn_regex = RegexValidator(regex=r'^\S*$',
                              message="SN must be ....不包含空字符")
    device_sn = models.CharField(validators=[sn_regex], blank=False, null=False, max_length=11, unique=True,
                                 verbose_name='设备SN')

    device_module = models.CharField(blank=False, null=False, max_length=100, verbose_name='设备型号')

    # 邮件,EmailField会校验邮件格式,最大长度50, 可以为空(注意:并没有min_length这个控制字段)
    # mail = models.EmailField(max_length=100, verbose_name='厂家联系邮件')

    # 设备类型,后面的为选择内容,前面为写入数据库的值, 注意max_length必须配置
    direction_choices = (
        ('router', '路由器'), ('switch', '交换机'), ('firewall', '防火墙'), ('other', '其他'))  # 数据库表约束，只能写入给定选择，和表单值匹配
    device_type = models.CharField(max_length=10, choices=direction_choices, blank=False, null=False,
                                   verbose_name='设备类型')

    # 最后一次修改时间，不可更改，系统自动创建
    update_date = models.DateTimeField(auto_now=True, verbose_name='最后一次修改时间')

    # 资料创建时间
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return f"{self.__class__.__name__}(device_name: {self.device_name} | device_sn: {self.device_sn}  | device_module: {self.device_module} | create_date: {self.create_date} | update_date: {self.update_date})"


class OPRS_DEVICE_Extension(models.Model):
    # 外键关联 关联OPRS_DEVICE_Base
    oprs_device_base = models.OneToOneField(OPRS_DEVICE_Base, related_name='oprs_device_extension', on_delete='CASCADE')

    device_init = models.BooleanField(default=False, verbose_name='设备在线状态')

    device_nas_ip = models.GenericIPAddressField(blank=False, null=False, unique=True, verbose_name='设备管理ip')

    Vendor = models.CharField(blank=True, null=True, max_length=10, verbose_name='设备厂商')

    # 最后一次修改时间，不可更改，系统自动创建
    update_date = models.DateTimeField(auto_now=True, verbose_name='最后一次修改时间')

    # 资料创建时间
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return f"{self.__class__.__name__}(device_init: {self.device_init} | device_nas_ip: {self.device_nas_ip} | Vendor: {self.Vendor})"


class OPRS_DEVICE_Tips(models.Model):
    # 外键关联 关联OPRS_DEVICE_Extension
    oprs_device_extension = models.OneToOneField(OPRS_DEVICE_Extension, related_name='oprs_device_tips',
                                                 on_delete='CASCADE')

    tips = models.TextField(blank=True, null=True, verbose_name='备注')

    def __str__(self):
        return f"{self.__class__.__name__}(tips: {self.tips})"


class OPRS_DEVICE_CPU_utli(models.Model):
    # 外键关联 关联OPRS_DEVICE_Base
    oprs_device_base = models.ForeignKey(OPRS_DEVICE_Base, related_name='oprs_device_cpu_utli', on_delete='CASCADE')

    cpu_utli = models.IntegerField(verbose_name='CPU利用率')

    # 资料创建时间
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return f"{self.__class__.__name__}(cpu_utli: {self.cpu_utli})"


class OPRS_DEVICE_Memory_utli(models.Model):
    # 外键关联 关联OPRS_DEVICE_Base
    oprs_device_base = models.ForeignKey(OPRS_DEVICE_Base, related_name='oprs_device_memory_utli', on_delete='CASCADE')

    memory_utli = models.IntegerField(verbose_name='memory利用率')

    # 资料创建时间
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return f"{self.__class__.__name__}(memory_utli: {self.memory_utli})"
