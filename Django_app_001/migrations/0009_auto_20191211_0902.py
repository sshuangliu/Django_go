# Generated by Django 2.2.7 on 2019-12-11 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Django_app_001', '0008_auto_20191211_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cpu_memory_utli',
            name='device_ip',
            field=models.GenericIPAddressField(verbose_name='设备管理ip'),
        ),
    ]
