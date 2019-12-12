from django.contrib import admin

# Register your models here.

# 创建管理员用户
# from  django.contrib.auth.models import User
# user = User.objects.create_superuser('admin', 'admin@xxoo.com', 'haha')

# 注册被管理的DB
from Django_app_001.models import OPRS_DB, CPU_memory_utli

admin.site.register(OPRS_DB)
admin.site.register(CPU_memory_utli)


# 查看后台用户的数据库权限：
# from django.contrib.auth.models import User
# a = User.objects.get(username='admin')
# a.get_all_permissions()
# {'auth.delete_user', 'admin.delete_logentry', 'Django_app_001.view_cpu_memory_utli', 'Django_app_001.delete_cpu_memory_utli', 'Django_app_001.add_oprs_db', 'auth.change_user', 'contenttypes.view_contenttype', 'sessions.view_session', 'sessions.add_session', 'Django_sub_001.change_studentsdb', 'auth.change_group', 'auth.change_permission', 'auth.view_group', 'contenttypes.delete_contenttype', 'Django_app_001.add_cpu_memory_utli', 'Django_app_001.change_oprs_db', 'auth.delete_group', 'Django_sub_001.add_department', 'contenttypes.change_contenttype', 'auth.view_user', 'Django_sub_001.delete_studentsdb', 'Django_sub_001.change_department', 'auth.add_permission', 'sessions.change_session', 'Django_sub_001.add_studentsdb', 'Django_app_001.delete_oprs_db', 'Django_app_001.view_oprs_db', 'Django_app_001.change_cpu_memory_utli', 'auth.view_permission', 'auth.add_user', 'Django_sub_001.delete_department', 'Django_sub_001.view_department', 'admin.view_logentry', 'contenttypes.add_contenttype', 'Django_sub_001.view_studentsdb', 'sessions.delete_session', 'auth.add_group', 'admin.add_logentry', 'admin.change_logentry', 'auth.delete_permission'}
# a = User.objects.get(username='t1')
# a.get_all_permissions()
# {'Django_app_001.view_oprs_db'}
