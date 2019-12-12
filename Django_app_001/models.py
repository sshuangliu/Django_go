from django.db import models
from django.core.validators import RegexValidator


# python3 manage.py startapp Django_sub_001app  创建子系统APP
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

class OPRS_DB(models.Model):
    device_name = models.CharField(max_length=100, verbose_name='设备名', unique=True)
    # SN,校验不包含空类型字符,最大长度为11,不可以为空,唯一键(注意:并没有min_length这个控制字段)
    sn_regex = RegexValidator(regex=r'^\S*$',
                              message="SN must be ....")
    device_sn = models.CharField(validators=[sn_regex], max_length=11, blank=False, unique=True)

    device_ip = models.GenericIPAddressField(blank=False, null=False, unique=True, verbose_name='设备管理ip')

    # 邮件,EmailField会校验邮件格式,最大长度50, 可以为空(注意:并没有min_length这个控制字段)
    mail = models.EmailField(max_length=100, verbose_name='厂家联系邮件')

    # 设备类型,后面的为选择内容,前面为写入数据库的值, 注意max_length必须配置
    direction_choices = (('router', '路由器'), ('switch', '交换机'))  #  数据库表约束，只能写入给定选择，和表单值匹配
    device_type = models.CharField(max_length=10, choices=direction_choices)


    # 纳管情况,后面的为选择内容,前面为写入数据库的值, 注意max_length必须配置
    payed_choices = ((True, '已纳管'), (False, '未纳管'))
    device_op = models.BooleanField(default=False, choices=payed_choices)

    # 资料更新时间
    create_date = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    # 资料更新时间
    update_date = models.DateTimeField(auto_now_add=True, verbose_name='修改时间')

    # 备注
    tips = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.__class__.__name__}(device_name: {self.device_name} | device_sn: {self.device_sn} | device_ip: {self.device_ip} | mail: {self.mail} | device_type: {self.device_type} | device_op: {self.device_op} | create_date: {self.create_date} | update_date: {self.update_date})"


class CPU_memory_utli(models.Model):

    device_name = models.CharField(max_length=100, verbose_name='设备名')

    device_ip = models.GenericIPAddressField(blank=False, null=False, verbose_name='设备管理ip')

    cpu_utli = models.IntegerField(verbose_name='CPU利用率')

    memory_utli = models.IntegerField(verbose_name='memory利用率')

    create_date = models.DateTimeField(auto_now=True, verbose_name='采集时间')